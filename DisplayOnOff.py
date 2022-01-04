import os
import time
import datetime
theTime = datetime.datetime.now().strftime('%Y%m%d_%H%M')

try:
    path=os.path.abspath('.')+"\Display"
    if not os.path.isdir(path):
        os.mkdir(path)
except :
 print("Error!Error!")
 
record=path+r"\OnOffTest_"+theTime+".txt"

#Cycle#
a=input("請輸入執行Display On/Off的次數(每3秒一個動作 ):  ")
for i in range(0,int(a)):
 print('<',i+1,"ROUND>")
 
 #Execute command <Mem>#
 os.system(r'adb shell "su 0 dp displayon"')
 temp=os.popen(r'adb shell "su 0 dp panelstatus"')
 text=temp.read()
 file1=open(record,"a")
 file1.write("ROUND"+str(i+1)+"\n"+str(text[53:57])+"\n")
 file1.close()
 temp.close()
  
 print(text[53:57])
 
 time.sleep(3)
 os.system(r'adb shell "su 0 dp displayoff"')
 temp=os.popen(r'adb shell "su 0 dp panelstatus"')
 text=temp.read()
 file1=open(record,"a")
 file1.write(str(text[53:57])+"\n"+"\n")
 file1.close()
 temp.close()

 print(text[53:57])
 
 time.sleep(3)
 
 
print("執行結束")
os.system("pause")