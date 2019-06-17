import os
import docker
apikey = input("enter apikey: ") 
a=1 
while(a==1): 
    mac = input("enter macaddress: ") 
    os.system('docker build -t navya .')
    client = docker.from_env() 
    #docker_path = "/home/navya/MacAddress"
    #image = client.image.build(path=docker_path, tag=test) 
    client.container.run(get('navya:latest'), command=(apikey,mac))
    a = input("do you want check another mac if yes enter 1 otherwise enter 0: ")
