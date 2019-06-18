import requests
import json
import sys
try:
  apikey=sys.argv[1]
  MacAddress=sys.argv[2]
  url = 'https://api.macaddress.io/v1'
  params = dict(
      output='json'
  )                                                                                                                                                                                        
  params['search']=MacAddress
  params['apikey']=apikey
  resp = requests.get(url=url, params=params)                                                                                                                                               
  info = resp.json()    
except Exception as e:
  print(e)
else:
  print("MAC Address " + MacAddress+ " is associated with "+info['vendorDetails']['companyName'] )
