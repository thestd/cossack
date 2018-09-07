from telegram.ext import Updater, CommandHandler, RegexHandler
from Bot_manager.home import BotManagerHome
from Bot_manager.nginx import BotManagerNginx
import settings as set

updater = Updater(token=set.TOKEN)
dispatcher = updater.dispatcher

nx = BotManagerNginx()
home = BotManagerHome()


# ********* HOME DISPATCH *********
start_hand = CommandHandler('start', home.home_menu)
dispatcher.add_handler(start_hand)

nginx_hand = RegexHandler('NGINX', nx.nginx_menu)
dispatcher.add_handler(nginx_hand)

about_os_hand = RegexHandler('About OS', home.about_os)
dispatcher.add_handler(about_os_hand)


# ********* NGINX DISPATCH *********
restart_nginx_hand = RegexHandler('restart/start nginx', nx.restart_nginx)
dispatcher.add_handler(restart_nginx_hand)

start_nginx_hand = RegexHandler('start nginx', nx.start_nginx)
dispatcher.add_handler(start_nginx_hand)

stop_nginx_hand = RegexHandler('stop nginx', nx.stop_nginx)
dispatcher.add_handler(stop_nginx_hand)

status_nginx_hand = RegexHandler('status nginx', nx.status_nginx)
dispatcher.add_handler(status_nginx_hand)

enabled_hosts_hand = RegexHandler('enabled hosts', nx.enabled_hosts)
dispatcher.add_handler(enabled_hosts_hand)

home_hand = RegexHandler('Back to home', home.home_menu)
dispatcher.add_handler(home_hand)


updater.start_polling()

