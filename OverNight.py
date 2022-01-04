import os
import time

for i in range(0,12):
 print('<',i+1,'>')
 file1 = open(r"C:\Users\PQT2\Desktop\MemTest.txt","a") 
 file1.write("=============<"+str(i+1)+">=============\n")
 file1.close()
 os.system(r"adb shell cat proc/meminfo >> C:\Users\PQT2\Desktop\MemTest.txt")
 file1 = open(r"C:\Users\PQT2\Desktop\MemTest.txt","a") 
 file1.write("\n")
 file1.close()
 time.sleep(3600)