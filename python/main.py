#Подключение библиотек
import telebot
import json
import mysql.connector
import requests
import urllib.request
import os
import time
from datetime import datetime
from telebot import types
from threading import Thread

# Подключение своих файлов
from BD_query import BD_query
from BD_query import get_sql
from config import TOKEN
from config import mysql_config
  
# Подключение у боту в базе данных
while True:
    try:
        bot = telebot.TeleBot(TOKEN)
        get_sql(**mysql_config)
        break
    except HTTPSConnectionPool as err:
        print(err)

# Обработчик присланных пользователем сообщений
@bot.message_handler(content_types=['text'])
def main1(message):
	print(1)

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e) 
        time.sleep(15)
    