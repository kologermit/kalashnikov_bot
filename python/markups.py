from telebot import types
def markups(commands, resize=True):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=resize)
    if not resize:
        for key in commands:
            markup.add(types.KeyboardButton(key))
    else:
        for i in range(len(commands)):
            commands[i] = (types.KeyboardButton(commands[i]))
        markup.add(*commands)
    markup.add(types.KeyboardButton("Меню"))
    return markup