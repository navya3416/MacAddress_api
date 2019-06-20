PROJECT DESCRIPTION
============================

   This project about program that will query https://macaddress.io ,returning with output MACaddress associated with which company and dockerize the above program that will take command line arguments.
   
Prerequisites
==========================
  1. Any Linux server(mine is ubuntu 16.04) with Docker installed.Refer the document to install the docker https://docs.docker.com/install/linux/docker-ce/ubuntu/ 
  
  
  2. Install python3 and pip and pip module docker
  
  
  3.signup in https://macaddress.io and get the apikey to used in program to generate the output.


Usage
=====================================
 Here having python script <mac_utility.py> to automate the docker image buildingand running process.Now run the above script.


                                 python3 mac_utility.py  
 
       when you run above command it will ask to prompt the apikey and give apikey value 
         
                               enter apikey: <your api key>

       After that it will ask about to prompt mac address give mac address which you want search
       
                              enter macaddress: <give the mac address which you want to search>                         

       Output is Like
       
                    Mac Address 44:38:39:ff:ef:57  is associated with Cumulus Networks, Inc
                    do you want check another mac if yes enter 1 otherwise enter 0: 
  
      If you want check another Mac Address enter 1 dont want enter 0
      
 If user found any difficult run the script when user type Help it will show READme.md file
    
                                        python3 mac_utility.py Help
     
