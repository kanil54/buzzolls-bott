import requests
from bs4 import BeautifulSoup
import telebot
import time

TOKEN = "8491944855:AAFz0r4DJ8nPTSKz5lBUP4jLdonBPCHsn6o"
"
CHAT_ID = 1229577244

URL = "https://it.buzzolls.ru/Courier/Home"

bot = telebot.TeleBot(TOKEN)
bot.send_message(CHAT_ID, "✅ Бот запущен")

sent_orders = set()

def check_orders():

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(URL, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    orders = soup.find_all(string=lambda t: "Заказ №" in t)

    for order in orders:

        text = order.strip()

        if text not in sent_orders:

            sent_orders.add(text)

            bot.send_message(CHAT_ID, f"🚨 Новый заказ\n\n{text}")

while True:

    try:
        check_orders()
    except Exception as e:
        print(e)

    time.sleep(15)
