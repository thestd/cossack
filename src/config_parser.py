import configparser


class BotConfig:
    def __init__(self, token):
        self.token = token


class OSConfig:
    def __init__(self, sudo_user, sudo_password):
        self.sudo_user = sudo_user
        self.sudo_password = sudo_password


class Config:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self._get_config()

        self.bot = BotConfig(token=self.__config['Bot_config']['bot_token'])
        self.os = OSConfig(
            sudo_user=self.__config['OS_config']['sudo_user'],
            sudo_password=self.__config['OS_config']['sudo_password']
        )

    def _get_config(self):

        if self.__config.read("local_config.ini"):
            pass

        elif self.__config.read("config.ini"):
            pass

        else:
            print("Не знайдено жодного config.ini")




