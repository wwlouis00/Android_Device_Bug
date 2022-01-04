import os

#Cycle#
for i in range(5):
    a=input("請輸入0為關閉，1為開啟:  ")
    if int(a) == 0:
        print("您輸入的為0")
        os.system(r"adb shell setprop persist.horus.disable.rk 0")
        break
    if int(a) == 1:
        print("您輸入的為1")
        os.system(r"adb shell setprop persist.horus.disable.rk 1")
        break
    else:
        print("《您輸入不正確的值，請重新輸入！》")
        i = i-1
        continue
os.system(r"adb reboot")
os.system("pause")
