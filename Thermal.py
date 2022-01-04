import os
import time
import datetime

TestTime = datetime.datetime.now().strftime('%Y%m%d_%H%M')

try:
    path = os.path.abspath('.') + "\Thermal_Test"
    if not os.path.isdir(path):
        os.mkdir(path)
except :
 print("Error! Could not create " + path)
 

thermal = path + r"\Thermal_"+ TestTime +".txt"
print("[Path] " + thermal + '\n')

Thermallist = ['7', '8', '9', '10', '12', '13', '14', '15']

time.sleep(180)

for i in range(8):
    os.system(r"ECHO " + "adb shell cat /sys/class/thermal/thermal_zone" + Thermallist[i] + "/temp >> " + thermal)
    os.system(r"adb shell cat /sys/class/thermal/thermal_zone" + Thermallist[i] + "/temp >> " + thermal)
    os.system(r"ECHO. >> " + thermal)

print("測試結束")
os.system("PAUSE")


