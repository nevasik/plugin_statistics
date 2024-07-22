from bot import TelegramBot

if __name__ == "__main__":
    bot = TelegramBot()
    try:
        bot.start()
    except KeyboardInterrupt:
        bot.stop()