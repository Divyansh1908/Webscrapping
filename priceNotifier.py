import requests
import pandas as pd
from bs4 import BeautifulSoup
import smtplib

re = requests.get('https://www.ebay.com/itm/182051560542?_trkparms=pageci%3A52ce8b9b-ae83-11ed-88e3-2ad97ff9edfd%7Cparentrq%3A5dd490371860a44d5c660110fffecf26%7Ciid%3A1')
reContent = re.content #get content of the url
# print(reContent) 

soup = BeautifulSoup(reContent, 'html.parser')
# print(soup.prettify())

price = soup.find_all('span', {"class": "ux-textspans"})
# price = soup.find(class_ = "ux-textspans")
wantPrices = []
words= 'US'
i=0
for prices in price:
    if(words in prices.get_text()):
        wantPrices.append(prices.get_text())

print(wantPrices[0][4:])

myPrice = float(wantPrices[0][4:])
print(type(myPrice))

if myPrice < 120:
    smt = smtplib.SMTP('smpt.gmail.com', 587)
    smt.ehlo()
    smt.starttls()
    smt.login('Your email', 'App password')
    smt.sendmail('From Email', 
                'To Email',
                f"Subject: Price Change Alert\n\n Hi, Price has dropped to {myPrice}")
    smt.quit()

