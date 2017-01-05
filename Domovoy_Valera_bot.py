# -*- coding: utf-8 -*-
import config  # импорт настроек
import telebot  # библиотека телебота
import logging  # библиотека журнала
import parse_bash  # функции для работы с баш.орг
import yandex_weather  # погода с яндекса
from telebot import types  # клавиатуры

# для запуска скриптов
# from subprocess import call

# настройки для журнала
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# создание бота с его токеном API
bot = telebot.TeleBot(config.token)

# текст справки
help_string = ["Это Валера *Мега бот*!\n\n", "/start - выводит приветствие;\n", "/help - отображает эту справку;\n"]


# --- команды

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'Привет, я Валера! Отправьте мне /help для вывод справки.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")


@bot.message_handler(commands=['server'])
def send_start(message):
    bot.send_message(message.chat.id, 'Кто здесь?')


@bot.message_handler(
    func=lambda message: message.text == 'Валера, настало твое время!' and message.content_type == 'text')
def valera_say(message):
    # msg = parse_bash.bash_get_quote_rnd(config.bash_url)
    msg = parse_bash.get_quote(config.bash_url)
    bot.send_message(message.chat.id, disable_web_page_preview="true", text=("%s" % msg), parse_mode="html")


@bot.message_handler(
    func=lambda message: message.text == 'Валера, сколько градусов?' and message.content_type == 'text')
def valera_say(message):
    # msg = parse_bash.bash_get_quote_rnd(config.bash_url)
    msg = yandex_weather.get_temp(config.ya_weather_url, 213)
    bot.send_message(message.chat.id, disable_web_page_preview="true", text=("%s" % msg), parse_mode="html")


# КЛАВИАТУРА
@bot.message_handler(
    func=lambda message: message.text == 'Валера' and message.content_type == 'text')
def valera_say(message):
    markup = types.ReplyKeyboardMarkup(True, True)
    markup.row('Валера, настало твое время!', 'Валера, сколько градусов?')
    markup.row('c', 'd', 'e')
    bot.send_message(message.chat.id, "Че надо?", reply_markup=markup)


# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#    bot.send_message(message.chat.id, message.text)


# запуск приёма сообщений
bot.polling()
