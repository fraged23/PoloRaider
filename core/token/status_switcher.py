from core.utils.logging import Logger
from core.utils.init import *

class StatusSwitcher:
    def __init__(self, theme):
        self.theme = theme
        self.logger = Logger(theme)

    def set_presence(self, token, name, details, state):
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        
        hd = json.loads(ws.recv())
        
        ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": platform.system(),
                    "$browser": "Polo",
                    "$device": "Polo"
                },
                "presence": {
                    "activities": [{
                        "name": name,
                        "type": 0,
                        "details": details,
                        "state": state
                    }],
                    "status": "online",
                    "since": 0,
                    "afk": False
                }
            }
        }))
        
        self.logger.success("SUCCESS", token)
        ws.close()

    def start(self):
        clear()
        print(ascii)
        print()
        
        with open('data/input/tokens.txt', 'r') as f:
            tokens = [token.strip() for token in f.readlines() if token.strip()]
            
        if not tokens:
            self.logger.error("NO TOKENS FOUND")
            return

        name = self.logger.input("NAME")
        details = self.logger.input("DETAILS")
        state = self.logger.input("STATE")
        
        for token in tokens:
            try:
                self.set_presence(token, name, details, state)
            except Exception as e:
                self.logger.error(f"ERROR: {str(e)}", token)
