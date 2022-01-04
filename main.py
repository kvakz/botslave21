import telebot
import random
from telebot import types


bot = telebot.TeleBot('token')

phrasesm = ["как всегда Вы прекрасны", "рад видеть Вас, мой день стал лучше!", "бля я заебался уже", "потрясающе выглядите, сеньор!", "я восхищен вашей красотой!!", "мой господин, лучше Вас нет никого!", "повелитель, для Вас я сделаю все что угодно!", "Ваше появление священно для меня!"]
phrasesf = ["как всегда Вы прекрасны", "рад видеть Вас, мой день стал лучше!", "бля я заебался уже", "потрясающе выглядите, мадам!", "я восхищен вашей красотой!!", "моя госпожа, лучше Вас нет никого!", "мисс, для Вас я сделаю все что угодно!", "Ваше появление священно для меня!", "правильно говорите, принцесса!"]
n = [0]  # список для определения рода(1,2,0) в нем один сравниваемый элемент


@bot.message_handler(commands=['start'])
def start_menu(message):
    del n[0]
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtnm = types.KeyboardButton('в мужском роде')
    itembtnf = types.KeyboardButton('в женском роде')
    markup.add(itembtnm, itembtnf)
    bot.send_message(chat_id=message.chat.id, text="добро пожаловать, как мне к Вам обращаться?", reply_markup=markup)
    bot.register_next_step_handler(message, send_phrase)


@bot.message_handler(content_types=['text'])
def send_phrase(message):
    if message.text == 'в мужском роде':
        n.append(1)
    elif message.text == 'в женском роде':
        n.append(2)
    else:
        n.append(0)
    print(n[0], message.text)

    if n[0] == 1:
        bot.send_message(chat_id=message.chat.id, text=random.choice(phrasesm))
    elif n[0] == 2:
        bot.send_message(chat_id=message.chat.id, text=random.choice(phrasesf))
    else:
        bot.send_message(chat_id=message.chat.id,
                         text="я запутался, напишите мне /start и определите в каком роде мне к Вам обращаться")
        del n[0]

    print(n[0], message.text, "второй прогон")


if __name__ == '__main__':
    print('Starting bot...')
    bot.polling(none_stop=True)
