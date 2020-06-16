from urllib.request import urlopen
from json import loads
from datetime import datetime
from time import sleep
import sys

def update(link):
    try:
        url = urlopen(link)
        data = loads(url.read())
        strdata = str(data)
        path = "assets/Data.txt"
        with open(path,"a",encoding="utf-8") as f:
            f.write(strdata)
        f.close()
    except:
        print("API RESPONSE ERROR...\nTry again in a while. We will continue from the page we left off.")
        input("Press any key to exit ")
        return False

if __name__ == "__main__":
    date = open("./assets/LastUpdatedOn.txt","r")
    DateAndTime = date.read()
    if(len(DateAndTime)!=0):
        print("Last Updated On " + DateAndTime)
    date.close()

    page = open("./assets/LastPage.txt","r")
    pageNo = page.read()
    if(len(pageNo)!=0):
        startAt = int(pageNo) + 1
    else:
        startAt = 0
    page.close()

    print("Update Process Started...\nThis might take a while. We will notify you once it is done.")
    lastUpdatedTill = 0
    for i in range(startAt,600):
        i = str(i)
        url = ("https://api.crackwatch.com/api/games?&is_cracked=true&page="+i)
        if update(url) is False:
            break
        print("Page " + i + " has been added")
        lastUpdatedTill = i

    print("Data has been successfully updated!")

    date = open("assets/LastUpdatedOn.txt","w")
    now = datetime.now()
    DateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")
    date.write(DateAndTime)
    date.close()

    page = open("assets/LastPage.txt","w")
    lastUpdatedTill = str(lastUpdatedTill)
    page.write(lastUpdatedTill)
    page.close()

    input("Press any key to exit ")
