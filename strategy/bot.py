import telebot
from API import *

a = f"Cумма достигла {x}"

bot = telebot.TeleBot('1724798563:AAFy0nHNECc3JL1ZnDCC_hXqnQVy8cV76LU')
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, a)
