import os, gspread, googlemaps, json
from dotenv import load_dotenv, find_dotenv
from pprint import pp

load_dotenv(find_dotenv())
API_KEY = os.getenv('API_KEY')
mapClient = googlemaps.Client(key=API_KEY)

def searchFor(category):
  response = mapClient.places(query=category)
  return response.get('results')

def writeBusinessDetails(listOfBusinesses, category):
  with open(f'./categories/{category}.json', 'w') as detailsFile:
    json.dump(listOfBusinesses, detailsFile)

def getAdditionalDetails(businessID):
  details = mapClient.place(place_id=businessID)
  phone = details["result"]["formatted_phone_number"]
  # website = details["result"]["website"]
  return phone

input = "pet-groomer"
results = searchFor(input)

businesses = []
for result in results:
  business = {
    'identifier': result['place_id'],
    'status': result['business_status'],
    'title': result['name'],
    'address': result['formatted_address'],
  }
  business['phone'] = getAdditionalDetails(business['identifier'])
  businesses.append(business)
writeBusinessDetails(businesses, input)


# sa = gspread.service_account(filename="svc-biz-list.json")
# sh = sa.open("Biz-List")
# wks = sh.worksheet("Sheet1")
