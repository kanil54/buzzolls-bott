import time
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

TOKEN = "8491944855:AAFz0r4DJ8nPTSKz5lBUP4jLdonBPCHsn6o"
CHAT_ID = 1229577244

bot = telebot.TeleBot(TOKEN)

URL = "https://it.buzzolls.ru/Courier/Home"

seen_orders = set()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

print("Бот запущен")

while True:
    try:
        orders = driver.find_elements(By.XPATH, "//*[contains(text(),'Заказ №')]")

        for order in orders:
            text = order.text

            if text not in seen_orders:
                seen_orders.add(text)

                bot.send_message(
                    CHAT_ID,
                    f"🚨 Новый заказ!\n{text}"
                )

        time.sleep(20)
        driver.refresh()

    except Exception as e:
        print(e)
