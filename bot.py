import telebot
import wikipedia


wikipedia.set_lang('uz')
bot = telebot.TeleBot('5046622194:AAHYf7aBaNvH8DJC1ngQBvevMQ2-1OA7lGQ')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hi and Welcome to the wikipedia, You can easily find any information in this bot! ')
@bot.message_handler(content_types=['text'])
def text(message):
    final=message.text.strip()
    try:
        mess=wikipedia.page(final).content
        if len(mess)>4096:
            for x in range(0,len(mess),4096):
                bot.send_message(message.chat.id,mess[x:x+4096])
        else:
            bot.send_message(message.chat.id,mess)
    except wikipedia.DisambiguationError:
        bot.send_message(message.chat.id,"Too many information found, Please write down clearly")
    except wikipedia.PageError:
        bot.send_message(message.chat.id,'Syntax Error ')
bot.polling()