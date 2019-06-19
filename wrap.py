# importing the modules
import os
import subprocess
import docker
import sys
# opening file READme.md when user type Help otherwise it will prompt to apikey
option=''
try:
 option=sys.argv[1]
except:
 pass
if option=='Help':
    file1 = open("README.md","r+")
    print (file1.read())
else:
#defining variable apikey for user input of apikey
    apikey = input("enter apikey: ")
    a = 1
# while loop for checking multiple mac address
    while(a==1):
# defining variable mac for user input of macaddress
        mac = input("enter macaddress: ")
# output will be redirected to stdout rather printing on the terminal and using subprocess execute docker commands
        process = subprocess.Popen(["docker","build", "-t", "navya","."], )stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        reader = csv.DictReader(stdout.decode('ascii').splitlines(),delimiter='|',skipinitialspace=True)
        for row in reader:
            output = json.dumps(row)
            print(output)
        subprocess.call(["docker","run","navya:latest",apikey,mac])
        a = int(input("do you want check another mac if yes enter 1 otherwise enter 0: "))
