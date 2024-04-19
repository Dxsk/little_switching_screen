import os
import sys


class Monitor:

    def __init__(self):
        self.display_switch:    str = 'C:\\Windows\\System32\\DisplaySwitch.exe'
        self.options: dict = {
            'extend':   f"{self.display_switch} /extend",
            'internal': f"{self.display_switch} /internal",
            'duplicate': f"{self.display_switch} /clone",
            'external': f"{self.display_switch} /external",
        }

    def switch_to(self, option: str) -> None:
        choice = self.options.get(option)
        if choice:
            os.system(choice)
        else:
            print(f"Options disponible : {list(self.options.keys())}")
            sys.exit(1)
