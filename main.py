import os, googlemaps, json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
API_KEY = os.getenv('API_KEY')
mapClient = googlemaps.Client(key=API_KEY)


def searchFor(category):
    response = mapClient.places(query=category)
    return response.get('results')


def writeToFile(listOfBusinesses, categoryFile):
    with open(f'./categories/{categoryFile}.json', 'w') as detailsFile:
        json.dump(listOfBusinesses, detailsFile)


def getAdditionalDetails(businessID):
    details = mapClient.place(place_id=businessID)
    phone = details["result"]["formatted_phone_number"]
    # website = details["result"]["website"]
    return phone


category = "pet-groomer"
results = searchFor(category)

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
writeToFile(businesses, category)
