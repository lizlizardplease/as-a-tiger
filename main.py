import telebot
import asyncio
from helpers import check_format, convert_format
from searcher import process_urls

bot = telebot.TeleBot('%токен%');

help_msg = "Чтобы своровать мптришку напиши /find \n \
            Чтобы послушать как я заебалась напиши /howru \n \
            Чтобы сходить за меня на отработку по физре напиши \
            мне на почту liz.nataljina@yandex.ru \n\
            Чтобы купить мне милкшейков скинь денег на 4274 3200 7595 3342"
@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, "Привет. Я бот.")
    bot.send_message(message.from_user.id, help_msg)
    if message.text == '/howru':
        bot.send_message(message.from_user.id, "ща на заебе, завтра скажу")
    if message.text == '/find':
        bot.send_message(
            message.from_user.id, 
            "Ща попробуем. Спроси в формате artist - song")
        bot.register_next_step_handler(message, try_find)
    else:
        bot.send_message(message.from_user.id, "Ну попросили же!")
        bot.send_message(message.from_user.id, help_msg)


def try_find(message): 
    song = message.text
    if not check_format(song):
        bot.send_message(message.from_user.id, "Ну попросили же!")
        bot.send_message(message.from_user.id, "В формате artist - song.")
        return
    ans = asyncio.run(process_urls(convert_format(song)))
    if ans:
        pass
        #print(ans)
        #bot.send_audio(ans)
    else:
        bot.send_message(message.from_user.id, "Чет не нашла")
    return 



bot.polling(none_stop=True, interval=0)