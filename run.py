import multiprocessing
import subprocess


# To run Bug
def startBug():
    # Code for process 1
    print("Process 1 is running...")
    from main import start
    start()

# To run hotword
def listenHotWord():
    # Code for process 2
    print("Process 2 is running...")
    from Backend.features import hotword
    hotword()

if __name__ == '__main__':
    startprocess = multiprocessing.Process(target=startBug)
    listenprocess = multiprocessing.Process(target=listenHotWord)
    startprocess.start()
    # subprocess.call(r'device.bat')
    listenprocess.start()
    startprocess.join()

    if listenprocess.is_alive():
        listenprocess.terminate()
        listenprocess.join()

    print("system stopped")