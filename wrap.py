import os
import subprocess
import docker
import sys
apikey = input("enter apikey: ")
a = 1
while(a==1):
    mac = input("enter macaddress: ")
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(["docker","build", "-t", "navya","."], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["docker","run","navya:latest",apikey,mac])
    a = int(input("do you want check another mac if yes enter 1 otherwise enter 0: "))
