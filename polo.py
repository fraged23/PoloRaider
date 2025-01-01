from core.utils.init import *
from core.server.spammer import *
from core.token.token_checker import *
from core.server.reply_spammer import *
from core.token.pronouns_switcher import *
from core.utils.logging import *
from core.token.bio_changer import *
from core.token.name_changer import *
from core.token.status_switcher import *

System.Size(125, 22)

def main_menu():
    options = {
        '1': Spammer(),
        '2': ReplySpammer(theme),
        '11': TokenChecker(theme),
        '15': NameSwitcher(theme), 
        '16': StatusSwitcher(theme),
        '17': PronounSwitcher(theme),
        '19': BioSwitcher(theme),
        '20': theme.change_theme
    }

    while True:
        colors = theme.get_colors()
        clear()
        print_logo()
        u_input = input(f"           {colors['main']}[{Colors.w}POLO{colors['main']}] {Colors.w}| {colors['main']}[{Colors.w}INPUT{colors['main']}] > ")

        if u_input in options:
            if u_input == '20':
                options[u_input]()
            else:
                options[u_input].start()

if __name__ == "__main__":
    main_menu()
