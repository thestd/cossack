from .os import OS
import settings as sett


class UFW(OS):
    def enable(self):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}ufw enable"
        return self.runner(cmd)

    def disable(self):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}ufw disable"
        return self.runner(cmd)

    def status(self, key='numbered'):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}ufw status {key}"
        return self.runner(cmd)

    def allow(self, port):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}ufw allow {port}"
        return self.runner(cmd)

    def deny(self, port):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}ufw deny {port}"
        return self.runner(cmd)

    def delete_rule(self, rule):
        cmd = f"{self.sudo(sett.SUDO_PASSWD)}ufw delete {rule}"
        return self.runner(cmd)

    def __str__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass