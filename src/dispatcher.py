from telegram.ext import Updater, CommandHandler, RegexHandler, CallbackQueryHandler
from src.bot.home import BotManagerHome
from src.bot.nginx import BotManagerNginx
from src.bot.ufw import BotManagerUfw
from src.bot.security import Security
from src.bot.shell import BotManagerShell
from src.config_parser import Config
from settings import settings, commands
import logging

config = Config()

updater = Updater(token=config.bot.token)
dispatcher = updater.dispatcher

nx = BotManagerNginx()
home = BotManagerHome()
ufw = BotManagerUfw()
security = Security()
shell = BotManagerShell()


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


# ********* NGINX DISPATCH *********
restart_nginx_hand = RegexHandler(commands.RESTART_NGINX, nx.restart_nginx)
dispatcher.add_handler(restart_nginx_hand)

start_nginx_hand = RegexHandler(commands.START_NGINX, nx.start_nginx)
dispatcher.add_handler(start_nginx_hand)

stop_nginx_hand = RegexHandler(commands.STOP_NGINX, nx.stop_nginx)
dispatcher.add_handler(stop_nginx_hand)

status_nginx_hand = RegexHandler(commands.STATUS_NGINX, nx.status_nginx)
dispatcher.add_handler(status_nginx_hand)

available_hosts_hand = RegexHandler(commands.GET_AVAILABLE_HOST, nx.get_available_hosts)
dispatcher.add_handler(available_hosts_hand)

enabled_hosts_hand = RegexHandler(commands.GET_ENABLED_HOST, nx.get_enabled_hosts)
dispatcher.add_handler(enabled_hosts_hand)

manage_host_hand = RegexHandler(commands.MANAGE_HOST, nx.manage_host)
dispatcher.add_handler(manage_host_hand)

enabling_host_hand = RegexHandler(commands.ENABLING_HOST, nx.enabling_host_menu)
dispatcher.add_handler(enabling_host_hand)

disabling_host_hand = RegexHandler(commands.DISABLING_HOST, nx.disabling_host_menu)
dispatcher.add_handler(disabling_host_hand)


# ********* UFW DISPATCH *********
enable_ufw_hand = RegexHandler('enable UFW', ufw.enable)
dispatcher.add_handler(enable_ufw_hand)

disable_ufw_hand = RegexHandler('disable UFW', ufw.disable)
dispatcher.add_handler(disable_ufw_hand)

status_ufw_hand = RegexHandler('status UFW', ufw.status)
dispatcher.add_handler(status_ufw_hand)


# ********* UFW DISPATCH *********
shell_hand = RegexHandler('Shell', shell.set_state_shell)
dispatcher.add_handler(shell_hand)

shell_runner_hand = RegexHandler('[\$] (.+)', shell.runner)
dispatcher.add_handler(shell_runner_hand)


# CALLBACK
security_keypad_hand = CallbackQueryHandler(security.check_code, pattern="(sec_.)")
dispatcher.add_handler(security_keypad_hand)

enabling_host_keypad_hand = CallbackQueryHandler(nx.enabling_host, pattern="(enabl_[\w.]+)")
dispatcher.add_handler(enabling_host_keypad_hand)

disabling_host_keypad_hand = CallbackQueryHandler(nx.disabling_host, pattern="(disabl_[\w.]+)")
dispatcher.add_handler(disabling_host_keypad_hand)

home_hand = RegexHandler(commands.BACK_TO_HOME, home.home_menu)
dispatcher.add_handler(home_hand)


# ========== LOGGING ==========
if settings.LOGGING_ENABLE:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)

    def error(bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)

    dispatcher.add_error_handler(error)
