# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

# текст справки
help_string = []
help_string.append("Это Валера *Мега бот*!\n\n")
help_string.append("/start - выводит приветствие;\n")
help_string.append("/help - отображает эту справку;\n")


# --- команды

@bot.message_handler(commands=['start'])
def send_start(message):
    # отправка простого сообщения
    bot.send_message(message.chat.id, 'Привет, я Валера! Отправьте мне /help для вывод справки.')


@bot.message_handler(commands=['help'])
def send_help(message):
    # отправка сообщения с поддержкой разметки Markdown
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")


@bot.message_handler(func=lambda message: message.text == "Валера")
def valera_say(message):
    bot.send_message(message.chat.id, 'Внимание, Анегдот!')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


bot.polling()
