import urllib.request
#import pyth
from time import sleep
import telebot

bot = telebot.TeleBot('5303402669:AAHjGYKBF2GGPd_xSx-b3GxR2P65ruvPO78')
  #sleep(0.5)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    url = "https://source.unsplash.com/random/?"+message.text
    filename = "image.png"
    urllib.request.urlretrieve(url, filename)
    bot.send_photo(message.chat.id, open('image.png', 'rb'))

if __name__ == '__main__':
     bot.infinity_polling()
