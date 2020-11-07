from BD_query import BD_query
from BD_query import get_sql
from config import mysql_config
def new_user(message):
	user = BD_query(get_sql(**mysql_config), "SELECT", "users", columns=["id", "name", "bot_status", "additional_parameter"], \
        where=[("id", "=", message.chat.id)], limit=1)
	if len(user) == 0:
		user = {
			"id": message.chat.id,
			"name": f"{message.chat.first_name} {message.chat.last_name}",
			"bot_status": 1,
			"additional_parameter": ""
		}
		BD_query(get_sql(**mysql_config), "INSERT", "users", data=[user])
	else:
		user = {
			"id": user[0][0],
			"name": user[0][1],
			"bot_status": user[0][2],
			"additional_parameter": user[0][3]
		}
	return user