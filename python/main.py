#Подключение библиотек
import telebot
import json
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
from new_user import new_user
from markups import markups
  
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

# Команда /start
@bot.message_handler(commands=["start"])
def start(message):
	# Создание нового пользователя, если такогого нет
	new_user(message)
	# Логгирование сообщений в окнсоль и БД
	log_query(get_sql(**mysql_config), 
		date=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
		chat_id=message.chat.id,
		first_name=message.chat.first_name,
		last_name=message.chat.last_name,
		text=message.text
	)
	# Ответ на полученный запрос
	bot.send_message(message.chat.id, answers["start"], reply_markup=start_markup())

# Основной обработчик присланных сообщений
@bot.message_handler(content_types=['text'])
def main1(message):
	# Создание нового пользователя, если такогого нет
	user = new_user(message)

	# Пребразование сообщение в нужный, для обработки вид
	message.text = message.text.strip()
	message_copy = message.text
	message.text = message.text.upper()

	# Логгирование сообщений в окнсоль и БД
	log_query(get_sql(**mysql_config), 
		date=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"),
		chat_id=message.chat.id,
		first_name=message.chat.first_name,
		last_name=message.chat.last_name,
		text=message.text
	)

	if (message.text == "ВОПРОС" and user["bot_status"] == 1):
		# Получение тем на вопросы из БД
		questions = BD_query(get_sql(**mysql_config), "SELECT", "questions", columns=["text"], where=[("last", "=", -1)])
		# Отправка ответа на запрос
		bot.send_message(message.chat.id, answers["question"], reply_markup=markups(list(key for key in questions[0])))
		# Изменение статуса в пользователя в БД 
		BD_query(get_sql(**mysql_config), "UPDATE", "users", data=[('bot_status', 2)], where=[("id", "=", message.chat.id)])
		return
	
	bot.send_message(message.chat.id, answers["invalid_request"])


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e) 
        time.sleep(15)
    