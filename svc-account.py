import glob, os, gspread
svcAccount = gspread.service_account(filename="svc-biz-list.json")
gSheet = svcAccount.open('Biz-List')


def getCategories(dir):
    categories = []
    os.chdir(dir)
    for file in glob.glob('*.json'):
        categories.append(os.path.splitext(file)[0])
    return categories


def createNewList(category):
  tabExists = False
  # check if False || throws an exception: "WorksheetNotFound: category"
  # tab = gSheet.worksheet(category)
  # if tab exists: return
  # if tabe does not exist
  # create the new tab

  # CREATES NEW TAB BUT THROWS ERR: "SHEET ALREADY EXISTS" even when !TRUE
  listOfTabs = gSheet.worksheets()
  for tab in listOfTabs:
      if not tab.title == category:
          gSheet.add_worksheet(title=category, rows=1, cols=1)


for category in getCategories('./categories'):
    createNewList(category)
