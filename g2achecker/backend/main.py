import requests
import re
import time
from mail import sendEmail
from bs4 import BeautifulSoup

# BASIC VALUES
# Can be used for different G2A websites
url = "https://www.g2a.com/nl-nl/nintendo-eshop-card-50-usd-nintendo-north-america-i10000006097010"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
# Change card price according to what you want
CARD_PRICE = 56.00
TIMER_TIME = 7200  # 2hours
priceArray = []


# This function checks the website for the price and then goes to the email class
def getPrice(passwd):
    print("test3")
    for foo in soup.find_all('div', attrs={'class': 'offer__details'}):
        print("test1")
        price = foo.find('span', attrs={'class': 'price'})
        print("test2" + price)
        price_text = price.text
        print("test3" + price_text)
        price_text = re.sub("E|U|R", "", price_text)
        print("test4" + price_text)
        price_float = float(price_text)
        print("test5" + price_float)
        priceArray.append(price_float)
        print("test6" + priceArray)

    lowest_price = min(priceArray)

    if lowest_price <= CARD_PRICE:
        sendEmail(lowest_price, url, passwd)
    time.sleep(TIMER_TIME)
    getPrice(passwd)


# main class that asks for your password
def main():
    passwd = input('Enter the password: ')
    getPrice(passwd)


if __name__ == '__main__':
    main()
