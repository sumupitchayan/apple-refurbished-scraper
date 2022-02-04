#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import os
from twilio.rest import Client

# WEB SCRAPING ----------------------------------------------------------------------

def scrapeSite():
    url = "https://www.apple.com/shop/refurbished/mac/macbook-air"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    parent = soup.find("body").find_all("li")

    macbooks = []

    for li in parent:
        price_div = li.find("div")

        # this means that it is an item for sale
        if price_div != None:

            a_link = li.find("a")

            # Gets the title, price, and link of items
            title = a_link.getText().encode('utf-8').strip()
            price = str(price_div.getText()).strip().replace('$', '').replace(',', '')
            price = float(price) if unicode(price, 'utf-8').isnumeric() else price
            link_ext = a_link["href"].encode('utf-8').strip()
            store_link = "apple.com" + link_ext

            # if it is a Macbook Air, then add to our list
            if "MacBook Air" in title and "2020" in title:
                item = {"title" : title, "price" : price, "link" : store_link}
                macbooks.append(item)
        
    print(macbooks)

# TWILIO ALERTS ---------------------------------------------------------------------

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# def sendText():
#     message = client.messages \
#     .create(
#          body='HERE IS A TEST MSG BABY',
#          from_='+19035517612',
#          to='+19175025772'
#      )

# -----------------------------------------

def main():
    scrapeSite()

if __name__ == "__main__":
    main()