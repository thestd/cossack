from telegram.ext import Updater, CommandHandler, RegexHandler, CallbackQueryHandler
from src.bot.home import BotManagerHome
from src.bot.nginx import BotManagerNginx
from src.bot.ufw import BotManagerUfw
from src.bot.security import Security
from src.config_parser import Config
from settings import settings
import logging

config = Config()

updater = Updater(token=config.bot.token)
dispatcher = updater.dispatcher

nx = BotManagerNginx()
home = BotManagerHome()
ufw = BotManagerUfw()
security = Security()


# ********* HOME DISPATCH *********
start_hand = CommandHandler('start', home.home_menu)
dispatcher.add_handler(start_hand)

nginx_hand = RegexHandler('NGINX', nx.nginx_menu)
dispatcher.add_handler(nginx_hand)

ufw_hand = RegexHandler('UFW', ufw.ufw_menu)
dispatcher.add_handler(ufw_hand)

about_os_hand = RegexHandler('About OS', home.about_os)
dispatcher.add_handler(about_os_hand)
#
security_hand = RegexHandler('security', security.send_menu)
dispatcher.add_handler(security_hand)

callback_handler = CallbackQueryHandler(security.check_code)
dispatcher.add_handler(callback_handler)


# ********* NGINX DISPATCH *********
restart_nginx_hand = RegexHandler('restart/start nginx', nx.restart_nginx)
dispatcher.add_handler(restart_nginx_hand)

start_nginx_hand = RegexHandler('start nginx', nx.start_nginx)
dispatcher.add_handler(start_nginx_hand)

stop_nginx_hand = RegexHandler('stop nginx', nx.stop_nginx)
dispatcher.add_handler(stop_nginx_hand)

status_nginx_hand = RegexHandler('status nginx', nx.status_nginx)
dispatcher.add_handler(status_nginx_hand)

available_hosts_hand = RegexHandler('get available hosts', nx.get_available_hosts)
dispatcher.add_handler(available_hosts_hand)

enabled_hosts_hand = RegexHandler('get enabled hosts', nx.enabled_hosts)
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


# ========== LOGGING ==========
if settings.LOGGING_ENABLE:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)

    def error(bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)

    dispatcher.add_error_handler(error)
