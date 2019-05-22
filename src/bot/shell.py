import telegram
from .security import protect_it
from src.os_manager.shell import Shell
from settings import commands, texts, states


class BotManagerShell:
    def __init__(self):
        self.shell = Shell()

    def set_state_shell(self, bot, update):
        states.SHELL_STATE = True
        bot.send_message(chat_id=update.message.chat_id,
                         text="Shell mode ON")

    @protect_it
    def runner(self, bot, update):

        bot.send_message(chat_id=update.message.chat_id,
                         text=self.shell.runner(update.message.text[1:]))
