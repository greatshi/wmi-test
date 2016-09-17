#coding=utf-8

import wmi

c = wmi.WMI()


for process in c.Win32_Process():
    print process.Name, process.ProcessId
    if process.Name == "cmd.exe":
        cmd = 1
    else:
        cmd = 0

print "*"*28
if cmd == 1:
    print "cmd.exe在运行！"
elif cmd == 0:
    print "cmd.exe没运行！"
print "*"*28
print "Over!"