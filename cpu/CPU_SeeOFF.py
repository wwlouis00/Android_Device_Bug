import os
import datetime

TestTime = datetime.datetime.now().strftime('%Y%m%d_%H%M')

try:
    path = os.path.abspath('.') + "\CPU_Usage_Test"
    if not os.path.isdir(path):
        os.mkdir(path)
except :
 print("Error! Could not create " + path)
 

logname = path + r"\CPU_SeeOFF_"+ TestTime +".txt"
print("[Path] " + logname + '\n')

Cputest = r"adb shell cpu_usage >> " + logname

os.system(Cputest)

print("End")
os.system("pause")