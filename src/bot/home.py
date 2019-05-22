from src.os_manager.os_manager import OS
import telegram


class BotManagerHome:
    def __init__(self):
        self.os = OS()
        self.custom_keyboard = [['NGINX', 'Shell'], ['About OS']]

    def home_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Home menu",
                         reply_markup=reply_markup)

    def about_os(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.os())
