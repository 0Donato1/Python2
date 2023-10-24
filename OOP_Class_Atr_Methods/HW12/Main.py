import requests
from bs4 import BeautifulSoup
import sqlite3

responsedeg = requests.get("https://meteo.ua/ua/34/kiev#2023-10-21--15-00")


if responsedeg.status_code == 200:
    soup = BeautifulSoup(responsedeg.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "weather-detail__main-degree"})
    if soup_list:
        result = soup_list[0].text.strip()


#DB----------------------------------------------------------------
db = sqlite3.connect('weather forecast.db')
sql = db.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users (Temperature TEXT)")

db.commit()

temperature = result

sql.execute(f"SELECT * FROM users")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES (?)", (temperature))
    db.commit()

    print("Nice")
else:
    print("Error")

    for value in sql.execute(f"SELECT * FROM users"):
        print(value)

