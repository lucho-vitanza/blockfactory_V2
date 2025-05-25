import telebot
from bot_telegram.config import BOT_TOKEN
from bot_telegram.handlers import register_handlers

print("handlers.py cargado")


bot = telebot.TeleBot(BOT_TOKEN)

def main():
    register_handlers(bot)
    print("Bot activo.")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
