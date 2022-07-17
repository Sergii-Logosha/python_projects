# Sergii Logosha, 18 Jun 2022

import urllib.request
import time

price = 99.99
while price > 4.74:
    time.sleep(900)
    # Requesting the website with coffee price
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    text = page.read().decode("utf8")

    # Printing out HTML text of the website
    print(text)

    # Extracting substring with the price from HTML string
    location = text.find(">$")
    price_start = location + 2
    price_end = location + 6
    price = float(text[price_start:price_end])
    print(price)
print("Buy!")
