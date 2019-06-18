# importing modules
import requests
import json
import sys
# giving the arguments for user input and giving the url and connecting to api with user given arguments
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
# exception handling     
except Exception as e:
  print(e)
# if not exception printing the output
else:
  print("MAC Address " + MacAddress+ " is associated with "+info['vendorDetails']['companyName'] )
