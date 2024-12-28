from core.utils.init import *
from core.utils.logging import *

class PronounSwitcher:
    def __init__(self, theme):
        self.theme = theme
        self.logger = Logger(theme)

    def start(self):
        clear()
        print(ascii)
        print()
        
        with open('data/input/tokens.txt', 'r') as f:
            tokens = [token.strip() for token in f.readlines() if token.strip()]
            
        if not tokens:
            self.logger.error("NO TOKENS FOUND")
            return
            
        pronouns = self.logger.input("PRONOUNS")
        
        for token in tokens:
            try:
                r = requests.patch(
                    'https://discord.com/api/v9/users/@me/profile',
                    headers={
                        'Authorization': token,
                        'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                    },
                    json={"pronouns": pronouns}
                )
                
                if r.status_code == 200:
                    self.logger.success("PRONOUNS CHANGED", token)
                elif r.status_code == 429:
                    self.logger.warning("RATE LIMITED", token)
                else:
                    self.logger.error("FAILED", token)
                    
            except Exception as e:
                self.logger.error(f"ERROR: {str(e)}", token)

                self.logger.msg("Press enter")
