from telebot import types
def markups(commands, resize=True):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=resize)
    for key in commands:
        if key["resize"] == True:
            markup.add(*(types.KeyboardButton(i) for i in key["commands"]))
        else:
            for i in key["commands"]:
                markup.add(types.KeyboardButton(i))
    return markup