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
from log_query import log_query
from start_markup import start_markup
  
# Подключение у боту в базе данных
while True:
    try:
        bot = telebot.TeleBot(TOKEN)
        get_sql(**mysql_config)
        break
    except HTTPSConnectionPool as err:
        print(err)

answers = (BD_query(get_sql(**mysql_config), "SELECT", "info", "text", where=[("theme", "=", "answers")])[0][0])
print(answers)
answers = json.loads(answers)

@bot.message_handler(commands=["start"])
def start(message):
	user = BD_query(get_sql(**mysql_config), "SELECT", "users", columns=["name"], \
        where=[("id", "=", message.chat.id)], limit=1)
	if len(user) == 0:
		BD_query(get_sql(**mysql_config), "INSERT", "users", data=[{
			"id": message.chat.id,
			"name": f"{message.chat.first_name} {message.chat.last_name}",
			"level": 1,
			"bot_status": 1,
			"additional_parameter": ""
		}])
	log_query(get_sql(**mysql_config), 
		date=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
		chat_id=message.chat.id,
		first_name=message.chat.first_name,
		last_name=message.chat.last_name,
		text=message.text
	)

	bot.send_message(message.chat.id, answers["start"], reply_markup=start_markup())
# Обработчик присланных пользователем сообщений
@bot.message_handler(content_types=['text'])
def main1(message):
	pass
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e) 
        time.sleep(15)
    