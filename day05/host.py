import os
import subprocess


ip = os.popen("ifconfig ens33|grep 'inet '|awk -F ' ' '{print $2}'|awk '{print $1}'")
for i in ip:
    print("ip地址为：%s" %(i.strip()))
def load_stat():
    with open("/proc/loadavg",'r')as f:
        con = f.read().split()
        print(con)
load_stat()