import telebot
import mainfile
BOT_TOKEN = "8609209708:AAFyG6H5J-LAZ4QPPczuWNxzAfmFGqJuqp8"

bot = telebot.TeleBot(BOT_TOKEN)
new_response=""
@bot.message_handler()
def get_chat_id(message):
    user_message= message.text
    module_response=mainfile.main(user_message)
    new_response=""
    try:
      user_message =message.text
      lenght=len(module_response)
      module_response=mainfile.main(user_message)
      lenght=len(module_response)
      #for i in range(len(module_response)):
      #  k= module_response[i]
      #  new_response= new_response+k
       # print(i)

         
    except Exception as k: 
      pass
    #   print(k)


    

    chat_id = message.chat.id
    bot.reply_to(message, module_response)

print("Bot is running...")
bot.infinity_polling()