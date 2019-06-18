import requests
import json
import sys
try:
  apikey=sys.argv[1]
  MacAddress=sys.argv[2]
except:
  print ("Enter apikey and macaddress as arguments")
url = 'https://api.macaddress.io/v1'
params = dict(
    output='json'
)
try:                                                                                                                                                                                        
  params['search']=MacAddress
  params['apikey']=apikey
  resp = requests.get(url=url, params=params)                                                                                                                                               
  info = resp.json()    
except:
  print("problem occurred while connecting to api")
else:
  print("MAC Address " + MacAddress+ " is associated with "+info['vendorDetails']['companyName'] )
