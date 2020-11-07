from BD_query import BD_query
import json
def log_query(sql, date, chat_id, first_name, last_name, text):
    print(date, chat_id, first_name, last_name, f"|{text}|")
    return BD_query(sql, "INSERT", "log_query", data=[{
        "text": json.dumps({"date": str(date), "chat_id": chat_id, "first_name": first_name, "last_name": last_name, "text": text}, indent=2)
    }])