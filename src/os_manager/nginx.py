from .os_manager import OS
from src.config_parser import Config

config = Config()


class Nginx(OS):
    def start(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'start')}"
        return self.runner(cmd)

    def restart(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'restart')}"
        return self.runner(cmd)

    def stop(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'stop')}"
        return self.runner(cmd)

    def status(self):
        cmd = f"{self.sudo(config.os.sudo_password)}{self.service('nginx', 'status')}"
        return self.runner(cmd, return_result=True)

    def enabled_hosts(self):
        cmd = f'grep "server_name " /etc/nginx/sites-enabled/*;'
        return self.runner(cmd, return_result=True) \
            .replace('#либо ip, либо доменное имя', '') \
            .replace('server_name ', '') \
            .replace(';', '')

    def get_available_host(self):
        return self.ls(path="/etc/nginx/sites-available/")

    def __str__(self):
        return self.status()

    def __call__(self, *args, **kwargs):
        return self.start()

