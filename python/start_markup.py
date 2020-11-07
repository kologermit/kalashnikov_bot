from telebot import types
def start_markup(commands=[]):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    arr = ["Вопрос"]
    for i in range(len(arr)):
        arr[i] = types.KeyboardButton(arr[i])
    for key in commands:
        arr.append(types.KeyboardButton(key))
    markup.add(*arr)
    return markup