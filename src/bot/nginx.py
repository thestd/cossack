import telegram
from .security import protect_it
from src.os_manager.nginx import Nginx


class BotManagerNginx:
    def __init__(self):
        self.nx = Nginx()
        self.custom_keyboard = [['restart/start nginx', 'stop nginx',], ['get available hosts', 'enabled hosts'],
                                ['manage hosts', 'status nginx'], ['Back to home']]

    def nginx_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="NGINX settings",
                         reply_markup=reply_markup)

    @protect_it
    def restart_nginx(self, bot, update):
        if self.nx.restart() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='NGINX [re]started')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    @protect_it
    def start_nginx(self, bot, update):
        if self.nx.start() == 0:
            bot.send_message(chat_id=update.message.chat_id, text='NGINX started')
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Failure')

    @protect_it
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

    def enabled_hosts(self, bot, update):
        resp = self.nx.enabled_hosts()
        bot.send_message(chat_id=update.message.chat_id, text=resp)

    def get_available_hosts(self, bot, update):
        resp = self.nx.get_available_host()
        bot.send_message(chat_id=update.message.chat_id, text=resp)