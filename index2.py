# Python 3 example using requests library.
import requests
from urllib import response
from bs4 import BeautifulSoup
import time
import math
from pathlib import Path
import certifi
import urllib3
import requests

count =0
def inc(): 
    global count 
    count += 1

API_URL = "https://api.zyte.com/v1/extract"
API_KEY = "0998c63df0e747eab8392a83c2f30ce9"
for page in range(53,163):
    while True:
        try:
            response = requests.post(API_URL, auth=(API_KEY, ''), json={
                "url": "https://www.immobilienscout24.de/Suche/de/sachsen/wohnung-kaufen?pagenumber=" + str(page),
                "browserHtml": True
                })
            data = response.json()
            # print(data)
            # print(data['browserHtml'])
            soup = BeautifulSoup(data['browserHtml'], "lxml")
            break
        except KeyError:
            time.sleep(3)
            print("Will try again for page ", str(page))
    # print(soup.prettify())
    for a in soup.find_all('a', attrs = {'data-go-to-expose-referrer':"RESULT_LIST_LISTING"}):
        href = a['href']
        print(href)
        inc()
        with open('Germany/Sachsen.txt', "a") as myfile:
            myfile.write(href + '\n')
    print("Appended all " + str(count) + " to page: " + str(page))
    
myfile.close()