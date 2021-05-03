import telebot
import os
import sys
import time
alpha="1209467284"
zahra="1285130975"
parcil="1293786817"
adddina="1320796684"
aditya="1299496627"
info_1IA03="-1001096100477"
jossie="1120613937"
def run():
    bot =telebot.TeleBot("1494592293:AAGw6yTDyGJFuL4pwYfwq5x-CRav0VSUiiQ",parse_mode=None)
    with open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\ListAkhir.txt'),'r') as isi:
        chat_id=jossie
        bot.send_message(chat_id,"Daftar tugas")
        message_temp=""
        for i in isi:
            if(i!='\n'):
                message_temp=message_temp+i+"\n"
            else:
                bot.send_message(chat_id,message_temp)
                message_temp=""
        #bot.send_message(chat_id,message_temp)

    #@bot.message_handler(func=lambda message: True)
    #def echo_all(message):
    #    print("id      : "+str(message.from_user.id))
    #    print("Nama    : "+message.from_user.first_name)
    #    print("Message : "+message.text)
    #    if message.text=="hello":
    #        bot.reply_to(message,"how are you")
    bot.polling()
if __name__=='__main__':
    run()
