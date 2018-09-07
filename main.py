from telegram.ext import Updater, CommandHandler, MessageHandler, Handler, filters, RegexHandler
from bot_func import *
import settings as set

updater = Updater(token=set.TOKEN)
dispatcher = updater.dispatcher

nx = ManageNginx()
home = Home()


# ********* HOME DISPATCH *********
start_hand = CommandHandler('start', home.home_menu)
dispatcher.add_handler(start_hand)

nginx_hand = RegexHandler('NGINX', nx.nginx_menu)
dispatcher.add_handler(nginx_hand)

about_os_hand = RegexHandler('About OS', home.about_os)
dispatcher.add_handler(about_os_hand)


# ********* NGINX DISPATCH *********
restart_nginx_hand = RegexHandler('restart NGINX', nx.restart_nginx)
dispatcher.add_handler(restart_nginx_hand)

start_nginx_hand = RegexHandler('start NGINX', nx.start_nginx)
dispatcher.add_handler(start_nginx_hand)

stop_nginx_hand = RegexHandler('stop NGINX', nx.stop_nginx)
dispatcher.add_handler(stop_nginx_hand)

status_nginx_hand = RegexHandler('status NGINX', nx.status_nginx)
dispatcher.add_handler(status_nginx_hand)

home_hand = RegexHandler('Back to home', home.home_menu)
dispatcher.add_handler(home_hand)


updater.start_polling()

