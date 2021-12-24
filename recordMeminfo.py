import os
import time
import re
import subprocess
import sys
import time
from datetime import datetime
get_time=datetime.now().strftime("%m%d%H%M")
#----------------------------
def getMeminfo(t):
    Result = get_time + "_MemAvailable_usage.txt"
 	while t:
        if t % 60 == 0:
            with open(Result, mode='a') as f:
                TS = str(subprocess.getoutput('adb shell date'))
                CheckMem = str(subprocess.getoutput('adb shell cat proc/meminfo'))
                Dumpsys = str(subprocess.getoutput('adb shell "dumpsys meminfo"'))
                f.write(TS + '\n')
                f.write(CheckMem + '\n\n')
                f.write(Dumpsys + '\n\n')
                for line in re.split(r"\n", CheckMem):
                    if "MemAvailable" in line:
                        MemA = line
                print("  - " + MemA)
        time.sleep(1)
        t -= 1
		
if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            test_time = int(sys.argv[1])
            getmeminfo(test_time)
        elif len(sys.argv) == 2 and sys.argv[1] == "?":
            print("How to use: \n    py " + sys.argv[0] + " [Test time (sec)]")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected.")

  
  
  
