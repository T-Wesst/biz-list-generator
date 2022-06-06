import os
from dotenv import load_dotenv, find_dotenv
import gspread
import googlemaps
from pprint import pp
import json

load_dotenv(find_dotenv())
API_KEY = os.getenv('API_KEY')
mapClient = googlemaps.Client(key=API_KEY)
# response = mapClient.places(query="pet groomer")
# results = response.get('results')
# pp(results[0])
# with open('biz.json', 'w') as biz:
#     json.dump(results, biz)
# with open('biz.json', 'r') as read_file:
#     datas = json.load(read_file)
# pp(datas)
# for data in datas:
# print(f'{data}\n')
# address = data.get('formatted_address')
# status = data.get('business_status')
# name = data.get('name')
# id = data.get('place_id')
detailsResults = mapClient.place(place_id="ChIJB40IZrSRwoARTC6QbhjaaKM")
with open('bizDetails.json', 'r') as read_file:
    bizDetails = json.load(read_file)
    phone = bizDetails["result"]["formatted_phone_number"]
    webiste = bizDetails["result"]["website"]
    print(phone, webiste)
    # phone = bizDetails.get("formatted_phone_number")
    # print(phone)

    # pp(details.get('website'))
    # phone = details.get('formatted_phone_number')
    # website = details.get('website')
    # with open('bizDetails.json', 'w') as biz:
    #     json.dump(detailsResults, biz)


# sa = gspread.service_account(filename="svc-biz-list.json")
# sh = sa.open("Biz-List")
# wks = sh.worksheet("Sheet1")
