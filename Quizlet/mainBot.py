#the code of the bot
import telegram.ext

Token = "6523200907:AAHSiPmj4wWIux0CaJxnJYaJHVZBALQMrdE"

updater = telegram.ext.updater(Token, use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello man")

def help(update, context):
    update.message.reply_text(" yo this is help")


dispatcher.add_handler(dispatcher )