# Biz-List Generator

A Python application that uses the Google Places API and Google Cloud Platform services accounts to search for businesses in differennt categories and write the information to Google Sheets.

## How it Works
1. supply the `searchFor` function with a business category `"pet-groomer"`. The response details are parsed for key details: `identifier, status, title, address` and written to a categories folder containing json files for each category.
2. Extract the `category filename` from the `categories directory` and use the GCP `service account` to write data to a sheet that corresponds to the category name.

Future Add-Ons
- Github Actions
  - schedule run scripts to automatically generate new sheets containing new business categories
- Chrome Extension
  - offering this service as a chrome extension reduces the time spent searching for and copying business details into a spreadsheet
- Templating Documents & Automations
  - explore the idea of using data in G-sheets to drafter contracts, project proposal and other documents