from config import TOKEN
import schedule
import time
from bot.bot import Bot
from sqldb import users_to_send
import pandas as pd


bot = Bot(token=TOKEN)
chats_to_send=users_to_send()


def send():
    cases = pd.read_csv('cases.csv', sep=",", index_col='Country/Other')
    for chat in chats_to_send:
        bot.send_text(chat_id=chat, text=f"Данные о заболевших COVID-19 по всему миру🌎:\n" \
                       f"Заболевших: {cases.loc['World', 'Total Cases']} ({cases.loc['World', 'New Cases']})\n" \
                       f"Смертей: {cases.loc['World', 'Total Deaths']} ({cases.loc['World', 'New Deaths']})\n" \
                       f"Выздоровело: {cases.loc['World', 'Total Recovered']}\n\n")


schedule.every(7).hours.do(send)

while True:
    schedule.run_pending()
    time.sleep(1)
