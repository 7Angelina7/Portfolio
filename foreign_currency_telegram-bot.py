'''Телеграмбот Rate_bot, который вытаскивает из сайта Центрального банка РФ актуальный курс юаней, долларов и евро.
Мгновенная информация о курсе в телеграмботе https://t.me/Yo_123_bot

Запуск бота: /start'''

import telebot
from bs4 import BeautifulSoup
import requests as req

bot = telebot.TeleBot('5847032878:AAEzzIi4Km4UnxXoRaZfQn4YccbykiONlWc')

main_url = 'https://cbr.ru/'
resp = req.get(main_url)
soup = BeautifulSoup(resp.text, 'lxml')

for i in soup.find_all('div', attrs={'class': 'main-indicator_rates-table'}):
    res = i.text

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f'Добро пожаловать в мгновенный сервис курса валют: {res}')


bot.polling(none_stop=True)