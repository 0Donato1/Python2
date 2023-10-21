import requests
from bs4 import BeautifulSoup

responsemin = requests.get("https://minfin.com.ua/ua/currency/usd/")
responsefin = requests.get("https://finance.i.ua")
responsekurs = requests.get("https://kurs.com.ua/ru/valyuta/gbp")

responsedeg = requests.get("https://meteo.ua/ua/34/kiev#2023-10-21--15-00")

time_or_currency = input(f"Choose what do you want to check \tcurrency, enter c  or \tweather, enter w: ")

if time_or_currency == "c":
    currency = input(f"USD - u "
                     f"\nEUR - e"
                     f"\nGBP - p"
                     f"\nChoose currency: ")

#USD-----------------------------------------------------------------------------------------------------------
    if(currency == "u"):
        operation = input(f"Buy - b"
                      f"\nSell - s"
                      f"\nChoose operation: ")

        if operation == "b":
            choose = int(input("Enter a number of US dollars: "))

            if responsemin.status_code == 200:
                soup = BeautifulSoup(responsemin.text, features="html.parser")
                soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
                time = soup_list[0]
                time_int = int(time.text[:2])
                result = time_int * choose
                print(f"{choose} US dollars is {result} grivnas")

        if operation == "s":
            choose = int(input("Enter a number of US dollars: "))

            if responsemin.status_code == 200:
                soup = BeautifulSoup(responsemin.text, features="html.parser")
                soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
                time = soup_list[2]
                time_int = int(time.text[:2])
                result = time_int * choose
                print(f"{choose} US dollars is {result} grivnas")

#EUR-----------------------------------------------------------------------------------------------------------

    if (currency == "e"):
        operation = input(f"Buy - b"
                          f"\nSell - s"
                          f"\nChoose operation: ")

        if operation == "b":
            choose = int(input("Enter a number of Euros: "))

            if responsefin.status_code == 200:
                soup = BeautifulSoup(responsefin.text, features="html.parser")
                soup_list = soup.find_all("span", {"class": "value -decrease"})
                time = soup_list[1]
                time_int = int(time.text[:2])
                result = time_int * choose
                print(f"{choose} euro is {result} grivnas")

        if operation == "s":
            choose = int(input("Enter a number of Euros: "))

            if responsefin.status_code == 200:
                soup = BeautifulSoup(responsefin.text, features="html.parser")
                soup_list = soup.find_all("span", {"class": "value -decrease"})
                time = soup_list[0]
                time_int = int(time.text[:2])
                result = time_int * choose
                print(f"{choose} euro is {result} grivnas")




#GBP-----------------------------------------------------------------------------------------------------------

    if (currency == "p"):
        operation = input(f"Buy - b"
                          f"\nSell - s"
                          f"\nChoose operation: ")

        if operation == "b":
            choose = int(input("Enter a number of Pounds: "))

            if responsekurs.status_code == 200:
                soup = BeautifulSoup(responsekurs.text, features="html.parser")
                soup_list = soup.find_all("div", {"class": "course"})
                time = soup_list[1]
                time_int = int(time.text[:2])
                result = time_int * choose
                print(f"{choose} pounds is {result} grivnas")

        if operation == "s":
            choose = int(input("Enter a number of Pounds: "))

            if responsekurs.status_code == 200:
                soup = BeautifulSoup(responsekurs.text, features="html.parser")
                soup_list = soup.find_all("div", {"class": "course"})
                time = soup_list[0]
                time_int = int(time.text[:2])
                result = time_int * choose
                print(f"{choose} pounds is {result} grivnas")


#WEATHER-----------------------------------------------------------------------------------------------------------

if time_or_currency == "w":
    if responsedeg.status_code == 200:
        soup = BeautifulSoup(responsedeg.text, features="html.parser")
        soup_list = soup.find_all("div", {"class": "weather-detail__main-degree"})
        if soup_list:
            result = soup_list[0].text.strip()
        print(f"{result} in Kyiv now")

with open(f"results.txt", "a") as file:
    file.write(f"\n{str(result)}")






