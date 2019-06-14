import requests
import json
import sys

try:
 apikey=sys.argv[1]
except IndexError:
 print("Apikey not found")

try:
 MacAddress=sys.argv[2]
except IndexError:
 print("Address not found")

url = 'https://api.macaddress.io/v1'
params = dict(
    output='json'
)

try:                                                                                                                                                                                        
  params['search']=MacAddress
  params['apikey']=apikey
except NameError:
 print("Something went wrong")

resp = requests.get(url=url, params=params)                                                                                                                                               
info = resp.json()    

try:
  print("MAC Addressis " + MacAddress+ " is associated with "+info['vendorDetails']['companyName'] )
except:
  print ("Data not found")
