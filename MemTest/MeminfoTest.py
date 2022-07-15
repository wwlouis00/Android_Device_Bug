import os
import time
import datetime
theTime = datetime.datetime.now().strftime('%Y%m%d_%H%M')

try:
    path=os.path.abspath('.')+"\MemTest"
    if not os.path.isdir(path):
        os.mkdir(path)
except :
 print("Error!Error!")
 
#Add time to export file#
filename=path+r"\MeminfoTest_"+theTime+".txt"
print("[Path] "+filename+'\n')

#grep value of MemTotal>, <MemAvailable> and <MemFree>#
Mem=r"adb shell grep -e MemTotal -e MemAvailable -e MemFree proc/meminfo >> "+filename

#Cycle#
a=input("請輸入分鐘(每5秒檢查1次 Memory Size):  ")
b=int(a)*60/5
for i in range(0,int(b)):
 print('<',i+1,"ROUND>")
 
 #Open filename with append mode and add round#
 file1 = open(filename,"a") 
 file1.write("<"+str(i+1)+">\n")
 file1.close()
  
 #Execute command <Mem>#
 os.system(Mem)
 
 #Open filename wiht append mode and change line#
 file1 = open(filename,"a") 
 file1.write("\n")
 file1.close()
 
 #Delay 5 seconds, you can set up time round from here#
 if i != int(b)-1: 
    time.sleep(5)

print("執行結束")
os.system("pause")