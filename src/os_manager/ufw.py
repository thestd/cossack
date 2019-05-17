from .os_manager import OS
from src.config_parser import Config

config = Config()


class UFW(OS):
    def enable(self):
        cmd = f"{self.sudo(config.os.sudo_password)}ufw enable"
        return self.runner(cmd)

    def disable(self):
        cmd = f"{self.sudo(config.os.sudo_password)}ufw disable"
        return self.runner(cmd)

    def status(self, key='numbered'):
        cmd = f"{self.sudo(config.os.sudo_password)}ufw status {key}"
        return self.runner(cmd)

    def allow(self, port):
        cmd = f"{self.sudo(config.os.sudo_password)}ufw allow {port}"
        return self.runner(cmd)

    def deny(self, port):
        cmd = f"{self.sudo(config.os.sudo_password)}ufw deny {port}"
        return self.runner(cmd)

    def delete_rule(self, rule):
        cmd = f"{self.sudo(config.os.sudo_password)}ufw delete {rule}"
        return self.runner(cmd)

    def __str__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass