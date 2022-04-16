from mytoken import token
from telegram.ext import Updater, CommandHandler
from handlers import next_prime, weather

def main() -> None:
    mybot = Updater(token, use_context=True) 

    mybot.dispatcher.add_handler(CommandHandler('next_prime', next_prime))
    mybot.dispatcher.add_handler(CommandHandler('weather', weather))
    print('ВСЁ ОК!')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
