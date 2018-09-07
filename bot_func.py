import os_manage as _
import telegram

class Home:
    def __init__(self):
        self.os = _.OS()
        self.custom_keyboard = [['NGINX'], ['About OS']]

    def home_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Home menu",
                         reply_markup=reply_markup)

    def about_os(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.os())

class ManageNginx:
    def __init__(self):
        self.nx = _.Nginx()
        self.custom_keyboard = [['start NGINX', 'restart NGINX'], ['stop NGINX', 'status NGINX'], ['Back to home']]

    def nginx_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                        text = "NGINX settings",
                        reply_markup = reply_markup)

    def restart_nginx(self, bot, update):
        if self.nx.restart() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='NGINX restarted')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    def start_nginx(self, bot, update):
        if self.nx.start() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='NGINX started')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    def stop_nginx(self, bot, update):
        if self.nx.stop() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='NGINX stopped')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    def status_nginx(self, bot, update):
        resp = self.nx.status()
        if resp[0] == 3:
            bot.send_message(chat_id=update.message.chat_id, text='Start the nginx first')
        else:
            bot.send_message(chat_id=update.message.chat_id, text=resp)




