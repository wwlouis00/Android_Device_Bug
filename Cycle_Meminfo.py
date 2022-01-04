import os
import time

Mem=r"adb shell grep -e MemAvailable -e MemFree proc/meminfo"

for i in range(0,3600):
    print("ROUND ",i+1," ==================")
    os.system(Mem)
    print("\n")
    time.sleep(1)