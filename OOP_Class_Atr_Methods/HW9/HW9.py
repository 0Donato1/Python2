import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

def get_weather_data():
    url = "https://ua.sinoptik.ua/погода-київ"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find('p', {'class': 'today-temp'}).text
        return temperature
    else:
        print("Помилка під час отримання даних з sinoptik.ua.")
        return None

conn = sqlite3.connect('погода.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS погода (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        датачас DATETIME,
        температура TEXT
    )
''')

now = datetime.now()
formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')

temperature = get_weather_data()

if temperature:
    cursor.execute('INSERT INTO погода (датачас, температура) VALUES (?, ?)', (formatted_date_time, temperature))
    conn.commit()
    print("Дані успішно додано до бази даних.")

conn.close()

'''
import requests
from bs4 import BeautifulSoup

response = requests.get("https://ua.sinoptik.ua")

# https://dateandtime.info/uk/city.php?id=703448

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "rSide"})
    time = soup_list[0]
    print(str(time.text))

else:
    print("404")
'''

