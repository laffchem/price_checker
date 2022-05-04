from bs4 import BeautifulSoup
import requests
from config import USER_KEY, APP_KEY

URL = "https://www.amazon.com/Logitech-Advanced-Wireless-Illuminated-Keyboard/dp/B07S92QBCJ"

#Headers to scrape Amazon.
headers = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS aarch64 14526.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
#Scrape MX Keys keyboard for lowest price
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

mx_price = soup.find(name="span", class_="a-offscreen")

price = mx_price.getText().replace('$', '')

#Check if price is lower than camelcamelcamel.com lowest price
if float(price) <= 100:
    message = "The price is right! Buy it now!"
else:
    message = "This shit is too expensive!"

#JSON Data for pushover app.
price_checker = {
    "token": APP_KEY,
    "user": USER_KEY,
    "message": message,
    "url": URL,
    "url_title": "MX Keys Keyboard",
}

response = requests.post("https://api.pushover.net/1/messages.json", json=price_checker)
print(response)
