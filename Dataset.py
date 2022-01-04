import os
import time
import datetime
import threading

TestTime = datetime.datetime.now().strftime('%Y%m%d_%H%M')

try:
    path = os.path.abspath('.') + "\Dataset_Test"
    if not os.path.isdir(path):
        os.mkdir(path)
except :
 print("Error! Could not create " + path)
 
Dataset = path + r"\Thermal_"+ TestTime +".txt"
print("[Path] " + Dataset + '\n')

print("Please close CU or SteamVR to START TEST")

global timer

def cupath():
    path = os.popen('where /R "c:\Program Files (x86)" ViveConsole.exe')
    global runcu
    runcu = path.read()
    runcu = runcu.strip()
    runcu = '"' + runcu + '"'
    path.close()

def exevr():
    print("====================== Please Run SteamVR NOW !! ======================")
    os.system(runcu)

def generate():
    print("=================== GENERATE NOW !!! PLEASE WAIT !! ===================")
    os.system(r"py C:\Users\PQT2\Desktop\Overall_Test_Tools\ParseDataset.py " + Dataset + " 600")

def closesteamvr():
    print("=================== CLOSE STEAMVR !! PLEASE WAIT !! ===================")
    os.system(r"ECHO TASKKILL /IM vrmonitor.exe")
    
timer = threading.Timer(0, cupath)
timer.start()

timer = threading.Timer(25, exevr)
timer.start()

timer = threading.Timer(629, closesteamvr)
timer.start()

timer = threading.Timer(630, generate)
timer.start()

print("Start Test!!")

os.system(r"adb shell su 0 stop horus-daemon")
os.system(r"adb shell su 0 horusd --ship 2  > " + Dataset)

