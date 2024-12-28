from core.utils.init import *

class Logger:
    def __init__(self, theme):
        self.theme = theme
        self.colors = theme.get_colors()
    
    def success(self, message: str, token: str = None):
        token_display = f"{self.colors['main']}[{Colors.w}{token[:25]}{self.colors['main']}]" if token else ""
        print(f"                                             {self.colors['main']}[{Colors.w}+{self.colors['main']}] {Fore.GREEN}{message} {token_display}")

    def valid(self, message: str, token: str = None):
        token_display = f"{self.colors['main']}[{Colors.w}{token[:25]}{self.colors['main']}]" if token else ""
        print(f"                                             {self.colors['main']}[{Colors.w}+{self.colors['main']}] {Colors.w}{message} {token_display}")

    def error(self, message: str, token: str = None):
        token_display = f"{self.colors['main']}[{Colors.w}{token[:25]}{self.colors['main']}]" if token else ""
        print(f"                                             {self.colors['main']}[{Colors.w}+{self.colors['main']}] {Fore.RED}{message} {token_display}")
    
    def warning(self, message: str, token: str = None):
        token_display = f"{self.colors['main']}[{Colors.w}{token[:25]}{self.colors['main']}]" if token else ""
        print(f"                                             {self.colors['main']}[{Colors.w}+{self.colors['main']}] {Fore.LIGHTRED_EX}{message} {token_display}")
    
    def input(self, message: str) -> str:
        return input(f"                                             {self.colors['main']}[{Colors.w}Polo{self.colors['main']}] {Colors.w}| {self.colors['main']}[{Colors.w}{message}{self.colors['main']}]{Colors.w} > ")
    
    def msg(self, message: str) -> str:
        return input(f"                                             {self.colors['main']}[{Colors.w}Polo{self.colors['main']}] {Colors.w}| {self.colors['main']}[{Colors.w}INPUT{self.colors['main']}]{Colors.w} {message} ")

    def useragent(self, message: str) -> str:
        return input(f"                            {self.colors['main']}[{Colors.w}POLO{self.colors['main']}] {Colors.w}| {self.colors['main']}[{Colors.w}DONE{self.colors['main']}] {Colors.w}{message} {self.cursor} ")