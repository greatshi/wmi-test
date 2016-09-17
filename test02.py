#coding=utf-8

import wmi

c = wmi.WMI()

def process_all():
    for process in c.Win32_Process():
        p_str = "进程名: " + str(process.Name) + "    进程ID: " + str(process.ProcessId)
        print unicode(p_str, 'utf-8')

def process_monitor(process_name):
    print "*" * 28
    process_running = 0
    for process in c.Win32_Process():
        if process.Name == process_name:
            p_str = process_name + "在运行！"
            print unicode(p_str, 'utf-8')
            process_running = 1
            break
    if process_running == 0:
        p_str = process_name + "没运行！"
        print unicode(p_str,'utf-8')
    print "*" * 28

    print "Over!"

def main():
    process_all()
    process_monitor("cmd.exe")
    process_monitor("python.exe")
    print unicode("按任意键退出~",'utf-8')
    s = raw_input()
if __name__ == "__main__":
    main()
