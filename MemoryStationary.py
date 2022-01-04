import os
import time
import datetime

TestTime = datetime.datetime.now().strftime('%Y%m%d_%H%M')

try:
    path = os.path.abspath('.') + "\MemOverall_Test"
    if not os.path.isdir(path):
        os.mkdir(path)
except :
 print("Error! Could not create " + path)
 

MemStationary = path + r"\MemStationary_"+ TestTime +".txt"
print("[Path] " + MemStationary + '\n')

# Origin
os.system(r"ECHO 【Origin】 >> " + MemStationary)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemStationary)
os.system(r"ECHO. >> " + MemStationary)

# 1 Minute
time.sleep(60)
os.system(r"ECHO 【1 Minute】 >> " + MemStationary)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemStationary)
os.system(r"ECHO. >> " + MemStationary)

# 2 Minute
time.sleep(60)
os.system(r"ECHO 【2 Minute】 >> " + MemStationary)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemStationary)
os.system(r"ECHO. >> " + MemStationary)

# 3 Minute
time.sleep(60)
os.system(r"ECHO 【3 Minute】 >> " + MemStationary)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemStationary)
os.system(r"ECHO. >> " + MemStationary)

# 5 Minute
time.sleep(120)
os.system(r"ECHO 【5 Minute】 >> " + MemStationary)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemStationary)
os.system(r"ECHO. >> " + MemStationary)

# 10 Minute
time.sleep(300)
os.system(r"ECHO 【10 Minute】 >> " + MemStationary)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemStationary)

print("測試結束")
os.system("PAUSE")