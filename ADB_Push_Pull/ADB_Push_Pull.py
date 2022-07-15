import os
import time

os.system(r"adb shell setprop persist.horus.rddevmode 1")
print("[Close CU or SteamVR to Start Test]●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system(r"ECHO TASKKILL /IM vrmonitor.exe")
print("[Please enter any key to start test when CU and SteamVR are closed]")
print("\n")
os.system(r"adb root")

print("[PUSH ITEM]●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system(r"ECHO [adb push C:\Users\PQT2\Desktop\SteamVR.url /storage]")
os.system(r"adb push C:\Users\PQT2\Desktop\SteamVR.url /storage")
print("\n")

print("[LIST Item]●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system(r"ECHO [adb shell ls storage]")
os.system(r"adb shell ls storage")
print("\n")

time.sleep(1)

print("[PULL ITEM]●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system(r"ECHO [adb pull /storage/SteamVR.url D:\Tools]")
os.system(r"adb pull /storage/SteamVR.url D:\Tools")
os.system(r"Start D:\Tools")
print("\n")

print("[PLEASE CHECK ITEM FROM FOLDER]●●●●●●●●●●●●●●●●●●●●●●●●●")
print("\n")

time.sleep(10)

print("[DELETE ITEM]●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system(r"ECHO [del D:\Tools\SteamVR.url]")
os.system(r"del D:\Tools\SteamVR.url")
os.system(r"ECHO [adb shell rm storage/SteamVR.url]")
os.system(r"adb shell rm storage/SteamVR.url")
print("\n")

print("[LIST Item]●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system(r"ECHO [adb shell ls storage]")
os.system(r"adb shell ls storage")
print("\n")

print("[請按任一按鍵執行 ADB REBOOT]●●●●●●●●●●●●●●●●●●●●●●●●●●")
os.system("pause")

os.system(r"adb reboot")

path = os.popen('where /R "c:\Program Files (x86)" ViveConsole.exe')
runcu = path.read()
path.close()

runcu = runcu.strip()
os.system(r'"' + runcu + '"')