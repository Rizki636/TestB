import os
import telebot
import requests
import json #bot rizki
from telebot import types

api = "2146702080:AAENzxW2_Bllpz40ZOtugIzzKs5LqoKiRDM"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=["start"])
def awal_bot(message):
    chatid = message.chat.id
    bot.send_photo(chatid, open('1566206027.png','rb'))
    tahap1 = types.InlineKeyboardMarkup()
    tahap2 = types.InlineKeyboardButton(text="CHANNEL STORE",url="https://t.me/AZ_Dan_Rizki_Store636")
    tahap3 = types.InlineKeyboardButton(text="GRUP",url="https://t.me/GrupDanaGratis")
    tahap4 = types.InlineKeyboardButton(text="CHANNEL UTAMA",url="https://t.me/ChannelDanaGratis")
    tahap5 = types.InlineKeyboardButton(text="CHANNEL DAGET",url="https://t.me/DanaKagetTeam")
    tahap1.add(tahap2)
    tahap1.add(tahap3,tahap4)
    tahap1.add(tahap5)
    bot.send_message(message.chat.id,"List Harga Yang Kami Jual\n===========\nYouTube Premium 4 Bulan = 3k\nYouTube Premium 1 Bulan = 1k\nNokos Telegram USA = 1.200\nNokos Telegram ID = 1.900\nNokos WhatsApp = 1k\n===========\nMinat Hubungi @Nokos_Rizki_Bot\n==========\nCommand yang tersedia di bot ini =\n/admin untuk melihat kontak admin",reply_markup=tahap1)
    bot.send_message(message.chat.id,"Bot By @Rizki636 --> Github --> Heroku --> Telegram")

@bot.message_handler(commands=["admin"])
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
    
@bot.message_handler(regexp='ga ngapa ngapain')
def text(message):
    bot.reply_to(message, """owh""")
    
@bot.message_handler(regexp='mau tanya sesuatu')
def text(message):
    bot.reply_to(message, """owh, ya udah lanjut tanya sana""")

@bot.message_handler(commands=['covidindo'])

def sambutan_start(message):
    api = requests.get('https://api.kawalcorona.com/indonesia/')
    api_json = api.json()
    api_content = api_json
    for wan in api_content:
         negara = api_content[0]['name']
         positif = api_content[0]['positif']
         sembuh = api_content[0]['sembuh']
         meninggal = api_content[0]['meninggal']
         dirawat = api_content[0]['dirawat']
         kirim = ('''
Negara = {}
Positif = {}
Sembuh = {}
Meninggal = {}
Dirawat = {}
'''.format(negara,positif,sembuh,meninggal,dirawat))
         bot.reply_to(message, kirim)
@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message,'ngapain kirim foto?')

@bot.message_handler(content_types=['document'])
def document(message):
    bot.reply_to(message,'ngapain kirim dokumen?')

@bot.message_handler(content_types=['text'])
def text(message):
    bot.reply_to(message,'perintah tersebut tidak ada di dalam bot')

@bot.message_handler(content_types=['video'])
def video(message):
    bot.reply_to(message,'ngapain kirim video disini?')

print("bot berjalan")

bot.polling()
