import requests
from bs4 import BeautifulSoup
import telebot
import time

TOKEN = "8491944855:AAFz0r4DJ8nPTSKz5lBUP4jLdonBPCHsn6o"
CHAT_ID = 1229577244

URL = "https://it.buzzolls.ru/Courier/Home"

bot = telebot.TeleBot(TOKEN)

seen_orders = set()

def check_orders():
    global seen_orders

    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "html.parser")

        orders = soup.find_all(string=lambda text: "Заказ №" in text)

        for order in orders:
            order_id = order.strip()

            if order_id not in seen_orders:
                seen_orders.add(order_id)

                bot.send_message(
                    CHAT_ID,
                    f"🚨 Новый заказ!\n{order_id}\n\nОткрой сайт чтобы принять."
                )

    except Exception as e:
        print(e)

print("Бот запущен")

while True:
    check_orders()
    time.sleep(20)
