import telegram
from OS_manager.ufw import UFW


class BotManagerUfw:
    def __init__(self):
        self.ufw = UFW()
        self.custom_keyboard = [['enable UFW', 'disable UFW',], ['status UFW', 'some button'], ['Back to home']]

    def ufw_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="UFW settings",
                         reply_markup=reply_markup)

    def enable(self, bot, update):
        if self.ufw.enable() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='UFW enabled')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    def disable(self, bot, update):
        if self.ufw.disable() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='UFW disabled')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    def status(self, bot, update):
        resp = self.ufw.status()
        # if resp[0] == 3:
        #     bot.send_message(chat_id=update.message.chat_id, text='Start the ngiufw first')
        # else:
        bot.send_message(chat_id=update.message.chat_id, text=resp)
