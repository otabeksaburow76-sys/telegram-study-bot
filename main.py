import telebot

TOKEN = 8741897093:AAHSqBZL88U87mu5g_C6TznYHDQewDEFx_E

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 📚\n"
        "O'quv yordamchi botiga xush kelibsiz!\n\n"
        "1. Slayd tayyorlash\n"
        "2. Mustaqil ish\n"
        "3. Referat\n"
        "4. PDF tayyorlash\n\n"
        "Kerakli mavzuni yozing."
    )

bot.infinity_polling()
