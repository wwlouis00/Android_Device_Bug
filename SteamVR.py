import os

p = os.popen('where /R "c:\Program Files (x86)" ViveConsole.exe')
print("TEST")

x = p.read()
x = '"' + x.strip() + '"'
print(x)
p.close()

os.system(x)

os.system("PAUSE")