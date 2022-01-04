import threading
import os

def fun_timer():
    print("Hello Timer!")
def run():
    os.system(r"adb logcat > ‪C:\Users\PQT2\Desktop\log.txt")

global timer
timer = threading.Timer(5, run)
timer.start()

timer = threading.Timer(1, fun_timer)
timer.start()

timer = threading.Timer(10, fun_timer)
timer.start()