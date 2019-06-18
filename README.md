PROJECT DESCRIPTION
============================

   This project about program that will query https://macaddress.io ,returning with output MACaddress associated with which company and dockerize the above program that will take command line arguments.
   
Prerequisites
==========================
  1. Any Linux server(mine is ubuntu 16.04) with Docker installed.Refer the document to install the docker https://docs.docker.com/install/linux/docker-ce/ubuntu/ 
  
  
  2. Install python3 and pip and pip module docker
  
  
  3.signup in https://macaddress.io and get the apikey to used in program to generate the output.
  
Getting Started
=======================================
 step 1: Take the above code mac.py 
 
 Step 2: Next will take the Dockerfile to dockerize the above program. In here we using multi-stage builds to build the Image.
       First stage build is the base image that will install all packages that need to execute the program.
       Second stage is to copy the program to working directory and used ENTRYPOINT configure to run time executable with the CMD to set
       additional default arguments of apikey and MAC Address
    
                   $ docker build -t <IMAGENAME:tag> . (or) $ docker build -t <IMAGENAME> <pathofDIR>
         
 Step 3: Run the above built image with the CMD arguments OF apikey and MAC Adderess
    
                  $docker run <IMAGENAME:tag> <APIKEY> <MACADDRESS>
                    
 output looks like :
                                                                                           
               Mac Address 44:38:39:ff:ef:57  is associated with Cumulus Networks, Inc

step 4: Here having python script <wrap.py> to automate the docker commands.Now run the above script.
st

                                 python3 wrap.py  
 
       when you run above command it will ask to prompt the apikey and give apikey value 
         
                               enter apikey: <your api key>

       After that it will ask about to prompt mac address give mac address which you want search
       
                              enter macaddress: <give the which you want to search>                         

       Output is Like
       
                    Mac Address 44:38:39:ff:ef:57  is associated with Cumulus Networks, Inc
                    do you want check another mac if yes enter 1 otherwise enter 0: 
  
      If you want check another Mac Address enter 1 dont want enter 0
      

step 5: if user found any difficult run the script when user type Help it will show READme.md file
    
                                        python3 wrap.py Help
     
