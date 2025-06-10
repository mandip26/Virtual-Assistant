from shlex import quote
from playsound import playsound
from Backend.config import ASSISTANT_NAME
from Backend.command import speak
from Backend.helper import extract_yt_term
from Backend.helper import remove_words
from hugchat import hugchat
import pyautogui
import subprocess
import os
import sqlite3
import struct
import time
import webbrowser
import pyaudio
import eel
import re
import pvporcupine
import pywhatkit as kit


con = sqlite3.connect('bug.db')
cursor = con.cursor()


# Play assistant sound function
@eel.expose
def playAssistantSound():
    music_dir = "Frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening" + query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening" + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening" + query)
                    try:
                        os.system('start ' + query)  # Added space after 'start'
                    except:
                        speak("not found")
        except:
            speak("something went wrong")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Pre-trained keywords
        porcupine = pvporcupine.create(keywords=["computer","bumblebee"],
                                       sensitivities=[0.6, 0.35])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        # Loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length, keyword)

            # Processing keyword comes from mic
            keyword_index = porcupine.process(keyword)

            # Checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                # Pressing shortcut key win+/
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("/")
                time.sleep(5)
                autogui.keyUp("win")
                print("hotword completed")

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# Find contacts
def findContact(query):

    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contact')
        return 0, 0

def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        bug_message = f"Message sent successfully to {name}"
    elif flag == 'call':
        target_tab = 7
        message = ''
        bug_message = f"Calling {name}"
    else:
        target_tab = 6
        message = ''
        bug_message = f"Starting video call with {name}"

    # Encode the message for URL
    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Open WhatsApp
    subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
    time.sleep(5)  # Wait for WhatsApp to open

    # Focus on the "Send" button
    pyautogui.hotkey('ctrl', 'f')
    for _ in range(1, target_tab):  # More readable loop
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')  # Press enter to send

    # Use the bug_message for feedback
    print(bug_message)  # Debugging output
    speak(bug_message)  # Provide feedback to the user

# chat bot
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="Backend\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

# Android automation
def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

def sendMessage(message, mobileNo, name):
    from Backend.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(5)
    time.sleep(1)
    keyEvent(3)
    # Open sms  app
    tapEvents(425, 1600)
    # Start chat
    tapEvents(840, 2220)
    # Search mobile no
    adbInput(mobileNo)
    # Tap on name
    tapEvents(601, 574)
    # Tap on input
    tapEvents(390, 2270)
    # Message
    adbInput(message)
    # Send
    tapEvents(957, 1310)
    speak("Message sent successfully to " + name)
