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
 

MemDynamic = path + r"\MemDynamic_"+ TestTime +".txt"
print("[Path] " + MemDynamic + '\n')

# Origin
os.system(r"ECHO 【Origin】 >> " + MemDynamic)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemDynamic)
os.system(r"ECHO. >> " + MemDynamic)

# 1 Minute
time.sleep(60)
os.system(r"ECHO 【1 Minute】 >> " + MemDynamic)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemDynamic)
os.system(r"ECHO. >> " + MemDynamic)

# 2 Minute
time.sleep(60)
os.system(r"ECHO 【2 Minute】 >> " + MemDynamic)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemDynamic)
os.system(r"ECHO. >> " + MemDynamic)

# 3 Minute
time.sleep(60)
os.system(r"ECHO 【3 Minute】 >> " + MemDynamic)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemDynamic)
os.system(r"ECHO. >> " + MemDynamic)

# 5 Minute
time.sleep(120)
os.system(r"ECHO 【5 Minute】 >> " + MemDynamic)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemDynamic)
os.system(r"ECHO. >> " + MemDynamic)

# 10 Minute
time.sleep(300)
os.system(r"ECHO 【10 Minute】 >> " + MemDynamic)
os.system(r"adb shell grep -e MemAvailable proc/meminfo >> " + MemDynamic)

print("測試結束")
os.system("PAUSE")