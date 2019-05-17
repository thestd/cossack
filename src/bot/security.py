import telegram
import settings
from src.config_parser import Config
from settings.texts import *

START_STATE = 0
UPDATE_STATE = 1
ERROR_STATE = 2
SUCCESS_STATE = 3
CLEAN_STATE = 4
CLOSE_STATE = 5

VALUE = 4


class Security:
    def __init__(self):
        self.config = Config()
        self.__pin_code = self.config.bot.pin_code
        self.__pin_counter = 0
        self.__len_pin = len(self.__pin_code)
        self.__matches = 0

    def send_menu(self, obj=None, bot=None, update=None, state=START_STATE):

        # if method not called in decorators
        if type(update) is int or not update:
            state = update
            update = bot
            bot = obj

        if state == START_STATE:
            update.message.reply_text(text=PIN_CODE_TEXT,
                                      reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                      parse_mode='HTML')
        elif state == UPDATE_STATE:
            bot.edit_message_text(text=PIN_CODE_TEXT+("*" * self.__pin_counter),
                                  reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        elif state == ERROR_STATE:
            bot.edit_message_text(text=PIN_CODE_TEXT + ("*" * self.__pin_counter) + ERROR_TEXT,
                                  reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        elif state == SUCCESS_STATE:
            bot.edit_message_text(text=SUCCESS_TEXT,
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        elif state == CLEAN_STATE:
            bot.edit_message_text(text=PIN_CODE_TEXT + CLEAN_FIELD_TEXT,
                                  reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        else:
            bot.edit_message_text(text=CLOSE_TEXT,
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

    def check_code(self, bot, update):
        data = update.callback_query.data

        if data[:4] == "sec_":
            if data[VALUE] == "<" or data[VALUE] == "x":
                self.__pin_counter = 0
                self.__matches = 0

                if data[VALUE] == "<":
                    self.send_menu(bot, update, CLEAN_STATE)
                elif data[VALUE] == "x":
                    self.send_menu(bot, update, CLOSE_STATE)

            else:
                self.__pin_counter += 1

                if self.__pin_code[self.__pin_counter - 1] == data[VALUE]:
                    self.__matches += 1

                if self.__pin_counter >= self.__len_pin:
                    if self.__matches == self.__len_pin:
                        from datetime import datetime
                        self.config.update_config(is_auth=1, last_auth=int(datetime.now().timestamp()))
                        self.send_menu(bot, update, SUCCESS_STATE)
                    else:
                        self.__pin_counter = 0
                        self.__matches = 0
                        self.send_menu(bot, update, ERROR_STATE)
                else:
                    self.send_menu(bot, update, UPDATE_STATE)


    @staticmethod
    def get_keypad():
        keypad = [
            [
                telegram.InlineKeyboardButton(1, callback_data=f'sec_1'),
                telegram.InlineKeyboardButton(2, callback_data=f'sec_2'),
                telegram.InlineKeyboardButton(3, callback_data=f'sec_3'),
            ],
            [
                telegram.InlineKeyboardButton(4, callback_data=f'sec_4'),
                telegram.InlineKeyboardButton(5, callback_data=f'sec_5'),
                telegram.InlineKeyboardButton(6, callback_data=f'sec_6'),
            ],
            [
                telegram.InlineKeyboardButton(7, callback_data=f'sec_7'),
                telegram.InlineKeyboardButton(8, callback_data=f'sec_8'),
                telegram.InlineKeyboardButton(9, callback_data=f'sec_9'),
            ],
            [
                telegram.InlineKeyboardButton("X", callback_data=f'sec_x'),
                telegram.InlineKeyboardButton(0, callback_data=f'sec_0'),
                telegram.InlineKeyboardButton("<-", callback_data=f'sec_<'),
            ],
        ]

        return keypad


def protect_it(func):
    """
    Decorator for protect bot function
    :param func: decorating function
    :return: decorator
    """
    from datetime import datetime

    def wrapper(*args, **kwargs):
        security = Security()

        # check the duration of the session.
        if (int(datetime.now().timestamp()) - security.config.auth.last_auth) >= settings.SESSION_DURATION:
            security.config.update_config(is_auth=0, last_auth=int(datetime.now().timestamp()))

        # decorating
        if security.config.auth.is_auth:
            func(*args, **kwargs)
        else:
            security.send_menu(*args, **kwargs)

    return wrapper
