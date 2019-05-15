from telegram.ext import Updater, CommandHandler, RegexHandler
from src.Bot_manager.home import BotManagerHome
from src.Bot_manager.nginx import BotManagerNginx
from src.Bot_manager.ufw import BotManagerUfw
from src.config_parser import Config

config = Config()

updater = Updater(token=config.bot_config.token)
dispatcher = updater.dispatcher

nx = BotManagerNginx()
home = BotManagerHome()
ufw = BotManagerUfw()


# ********* HOME DISPATCH *********
start_hand = CommandHandler('start', home.home_menu)
dispatcher.add_handler(start_hand)

nginx_hand = RegexHandler('NGINX', nx.nginx_menu)
dispatcher.add_handler(nginx_hand)

ufw_hand = RegexHandler('UFW', ufw.ufw_menu)
dispatcher.add_handler(ufw_hand)

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


# ********* UFW DISPATCH *********
enable_ufw_hand = RegexHandler('enable UFW', ufw.enable)
dispatcher.add_handler(enable_ufw_hand)

disable_ufw_hand = RegexHandler('disable UFW', ufw.disable)
dispatcher.add_handler(disable_ufw_hand)

status_ufw_hand = RegexHandler('status UFW', ufw.status)
dispatcher.add_handler(status_ufw_hand)


updater.start_polling()

