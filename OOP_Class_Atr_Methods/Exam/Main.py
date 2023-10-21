import requests
from bs4 import BeautifulSoup

response = requests.get("https://minfin.com.ua/ua/currency/usd/")

choose = int(input("Enter a number of US dollars: "))

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
    time = soup_list[2]
    time_int = int(time.text[:2])
    print(f"{choose} US dollars is {time_int * choose} grivnas")









