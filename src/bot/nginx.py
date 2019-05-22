import telegram
from .security import protect_it
from src.os_manager.nginx import Nginx
from settings import commands, texts


class BotManagerNginx:
    def __init__(self):
        self.nx = Nginx()
        self.custom_keyboard = [
            [commands.RESTART_NGINX, commands.STOP_NGINX,],
            [commands.GET_AVAILABLE_HOST, commands.GET_ENABLED_HOST],
            [commands.MANAGE_HOST, commands.STATUS_NGINX],
            [commands.BACK_TO_HOME]
        ]

        self.manage_host_keyboard = [
            [commands.ENABLING_HOST, commands.DISABLING_HOST],
            [commands.BACK_TO_HOME]
        ]

    def nginx_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="NGINX settings",
                         reply_markup=reply_markup)

    @protect_it
    def manage_host(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.manage_host_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Managing hosts NGINX",
                         reply_markup=reply_markup)

    @protect_it
    def restart_nginx(self, bot, update):
        chat_id = update.message.chat_id if update.message else update.callback_query.message.chat_id
        if self.nx.restart() == 0:
            bot.send_message(chat_id=chat_id, text='NGINX [re]started')
        else:
            bot.send_message(chat_id=chat_id, text='Failure')

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

    def get_enabled_hosts(self, bot, update):
        resp = self.nx.get_enabled_hosts()
        bot.send_message(chat_id=update.message.chat_id, text=resp)

    def get_available_hosts(self, bot, update):
        resp = self.nx.get_available_host()
        bot.send_message(chat_id=update.message.chat_id, text=resp)

    def enabling_host_menu(self, bot, update):
        host_keypad = []
        for host in self.nx.get_available_host().split():
            host_keypad.append(
                [telegram.InlineKeyboardButton(host, callback_data=f'enabl_{host}')]
            )

        update.message.reply_text(text=texts.CHOOSE_AVAILABLE_HOST,
                                  reply_markup= telegram.InlineKeyboardMarkup(host_keypad),
                                  parse_mode='HTML')

    def disabling_host_menu(self, bot, update):
        host_keypad = []
        for host in self.nx.get_enabled_hosts().split():
            host_keypad.append(
                [telegram.InlineKeyboardButton(host, callback_data=f'disabl_{host}')]
            )

        update.message.reply_text(text=texts.CHOOSE_AVAILABLE_HOST,
                                  reply_markup=telegram.InlineKeyboardMarkup(host_keypad),
                                  parse_mode='HTML')

    def enabling_host(self, bot, update):
        query = update.callback_query
        self.nx.enabling_host(query.data[6:])
        bot.edit_message_text(text=texts.HOST_ENABLED,
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              parse_mode='HTML')
        self.restart_nginx(bot, update)

    def disabling_host(self, bot, update):
        query = update.callback_query
        self.nx.disabling_host(query.data[7:])
        bot.edit_message_text(text=texts.HOST_ENABLED,
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              parse_mode='HTML')
        self.restart_nginx(bot, update)