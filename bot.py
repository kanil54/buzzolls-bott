import time
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

TOKEN = "ТВОЙ_ТОКЕН"
ADMIN_ID = 1229577244

bot = telebot.TeleBot(TOKEN)

url = "https://it.buzzolls.ru/Courier/Home"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get(url)

bot.send_message(ADMIN_ID, "✅ Бот запущен")

orders = []

while True:
    try:
        driver.refresh()
        time.sleep(5)

        page = driver.page_source

        if "Заказ" in page:
            if page not in orders:
                orders.append(page)

                bot.send_message(
                    ADMIN_ID,
                    "🚨 Новый заказ!\n\nПроверь панель курьера"
                )

        time.sleep(10)

    except Exception as e:
        print(e)
        time.sleep(10)
