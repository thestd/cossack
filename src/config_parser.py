import configparser
import settings

class BotConfig:
    def __init__(self, token, pin_code):
        self.token = token
        self.pin_code = pin_code


class OSConfig:
    def __init__(self, sudo_user, sudo_password):
        self.sudo_user = sudo_user
        self.sudo_password = sudo_password


class Auth:
    def __init__(self, is_auth, last_auth, session_duration):
        self.is_auth = is_auth
        self.last_auth = last_auth
        self.session_duration = session_duration


class Config:
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config_name = ''
        self._get_config()

        self.bot = BotConfig(
            token=self._config['Bot_config']['bot_token'],
            pin_code=self._config['Bot_config']['pin_code'],
        )
        self.os = OSConfig(
            sudo_user=self._config['OS_config']['sudo_user'],
            sudo_password=self._config['OS_config']['sudo_password'],
        )
        self.auth = Auth(
            is_auth=int(self._config['Auth']['is_auth']),       # boolean field
            last_auth=int(self._config['Auth']['last_auth']),   # datetime in timestamp
            session_duration=int(self._config['Auth']['session_duration']),   # datetime in timestamp
        )

    def _get_config(self):

        if self._config.read("local_config.ini"):
            self._config_name = "local_config.ini"

        elif self._config.read("config.ini"):
            self._config_name = "config.ini"

        else:
            print("Не знайдено жодного config.ini")

    def update_config(self, is_auth, last_auth):
        self._config['Auth'] = {'is_auth': is_auth, 'last_auth': last_auth,
                                'session_duration': settings.SESSION_DURATION}
                                # 'session_duration': self.auth.session_duration}

        with open(self._config_name, "w") as configure:
            self._config.write(configure)

        self.auth.is_auth = is_auth

