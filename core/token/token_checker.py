from core.utils.init import *
from core.utils.logging import Logger

class TokenChecker:
    def __init__(self, theme):
        self.theme = theme
        self.input_file = "data/input/tokens.txt"
        self.valid_output_file = "data/output/valid.txt"
        self.invalid_output_file = "data/output/invalid.txt"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.logger = Logger(theme)
        os.makedirs("data/output", exist_ok=True)

    def load_tokens(self):
        with open('data/input/tokens.txt', 'r') as f:
            return [token.strip() for token in f.readlines() if token.strip()]

    def check_token(self, token):
        self.headers["Authorization"] = token
        try:
            r = requests.get("https://discord.com/api/v9/users/@me", headers=self.headers)
            if r.status_code == 200:
                return "valid"
            elif r.status_code == 401:
                return "invalid"
            elif r.status_code == 429:
                return "rate_limited"
            elif "You need to verify your account" in r.text:
                return "locked"
            elif r.status_code == 403:
                return "locked"
            else:
                return "unknown"
        except Exception as e:
            return "error"

    def start(self):
        clear()
        print(ascii)
        print()
        tokens = self.load_tokens()
        clear()
        print(ascii)
        print()
        
        if not tokens:
            self.logger.error("Couldn't find any tokens, Returning.")
            self.logger.input("Press Enter")
            return

        valid_tokens = []
        invalid_tokens = []
        for i, token in enumerate(tokens, 1):
            status = self.check_token(token)

            if status == "valid":
                self.logger.valid("VALID", token)
                valid_tokens.append(token)
            elif status == "invalid":
                self.logger.error("INVALID", token)
                invalid_tokens.append(token)
            elif status == "rate_limited":
                self.logger.warning("RATE LIMITED", token)
            elif status == "locked":
                self.logger.error("LOCKED", token)
            else:
                self.logger.error("ERROR", token)

        time.sleep(2)
        clear()
        print(ascii)
        if valid_tokens or invalid_tokens:
            if valid_tokens:
                with open(self.valid_output_file, 'w') as f:
                    f.write('\n'.join(valid_tokens))
            if invalid_tokens:
                with open(self.invalid_output_file, 'w') as f:
                    f.write('\n'.join(invalid_tokens))
            print()
            self.logger.success("All valid/invalid tokens have been stored.")
            self.logger.input("Press Enter")
