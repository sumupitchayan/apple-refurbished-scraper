#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

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
            if "MacBook" in title:
                item = {"title" : title, "price" : price, "link" : store_link}
                macbooks.append(item)
    
    print(macbooks)

# -----------------------------------------

def main():
    scrapeSite()

if __name__ == "__main__":
    main()