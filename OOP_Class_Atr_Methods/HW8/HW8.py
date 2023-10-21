import requests
from bs4 import BeautifulSoup

response = requests.get("https://minfin.com.ua/ua/currency/usd/")

choose = int(input("Enter a number of grivnas you want to convert to US dollars: "))

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
    rate = soup_list[2]
    rate_int = int(rate.text[:2])
    print(f"{choose} grivnas is {choose / rate_int:.2f} US dollars")