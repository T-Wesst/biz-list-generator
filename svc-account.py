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
    listOfTabs = gSheet.worksheets()
    for tab in listOfTabs:
        if not tab.title == category:
            gSheet.add_worksheet(title=category, rows=1, cols=1)


for category in getCategories('./categories'):
    createNewList(category)
