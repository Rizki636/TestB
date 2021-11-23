import os
import telebot
import requests
import json #bot rizki
from telebot import types

api = "2146702080:AAENzxW2_Bllpz40ZOtugIzzKs5LqoKiRDM"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=["start"])
def awal_bot(message):
    dest1 = types.InlineKeyboardMarkup()
    dest2 = types.InlineKeyboardButton(text="KONTAK ADMIN",url="https://t.me/Rizki636")
    dest1.add(dest2)
    bot.send_message(message.chat.id,"ini adalah kontak admin",reply_markup=dest1)
    keybord1 = types.ReplyKeyboardMarkup()
    keybord2 = types.KeyboardButton(text="ga ngapa ngapain")
    keybord3 = types.KeyboardButton(text="mau tanya sesuatu")
    keybord1.add(keybord2,keybord3)
    bot.send_message(message.chat.id,"mau ngapain?, ko cari cari no admin?",reply_markup=keybord1)
    

print("bot berjalan")

bot.polling()
