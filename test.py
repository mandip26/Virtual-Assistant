# import pyautogui
# import subprocess
# import time
# from shlex import quote
#
# def whatsApp(mobile_no, message, flag, name):
#     if flag == 'message':
#         target_tab = 12
#         bug_message = f"Message sent successfully to {name}"
#     elif flag == 'call':
#         target_tab = 7
#         message = ''
#         bug_message = f"Calling {name}"
#     else:
#         target_tab = 6
#         message = ''
#         bug_message = f"Starting video call with {name}"
#
#     # Encode the message for URL
#     encoded_message = quote(message)
#     whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
#
#     # Open WhatsApp
#     subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
#     time.sleep(5)  # Wait for WhatsApp to open
#
#     # Focus on the "Send" button
#     pyautogui.hotkey('ctrl', 'f')
#     for _ in range(1, target_tab):  # More readable loop
#         pyautogui.hotkey('tab')
#         # time.sleep(0.2)  # Small delay for better accuracy
#
#     pyautogui.hotkey('enter')  # Press enter to send
#
#     print(bug_message)  # Debugging output
#
# # Example usage
# whatsApp(mobile_no="+917430835218", message="", flag="call", name="Ritika")
