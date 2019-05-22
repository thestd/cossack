from .os_manager import OS
from src.config_parser import Config

config = Config()


class Shell(OS):
    def run_command(self, command):
        sudo_mode = False
        if command[:4] == "sudo":
            sudo_mode = True

        cmd = f"{self.sudo(config.os.sudo_password) if sudo_mode else ''}{command}"
        return self.runner(cmd, return_result=True)