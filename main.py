import requests
from bs4 import BeautifulSoup

def spidex(maxpg):
    page=1
    while page<=maxpg:
        url="https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page="+str(page)+"&q=mobiles&viewType=list"
        code=requests.get(url)
        ptext=code.text
        soup=BeautifulSoup(ptext,"html.parser")
        for title in soup.findAll("a",{"class":"_1UoZlX"}):
            link="www.flipkart.com"+title.get("href")
            print(link)


        page+=1



spidex(2)