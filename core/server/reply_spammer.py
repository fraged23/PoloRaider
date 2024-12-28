from core.utils.init import *
from core.utils.logging import Logger

class ReplySpammer:
    def load_tokens(self):
        with open('data/input/tokens.txt', 'r') as f:
            return [token.strip() for token in f.readlines() if token.strip()]

    def __init__(self, theme):  
        self.theme = theme      
        self.tokens = self.load_tokens()
        self.headers = [
            {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            } for token in self.tokens
        ]
        self.stats = {
            "success": 0, 
            "failed": 0, 
            "ratelimited": 0}
        self.running = True
        self.logger = Logger(theme)

   
    def spam_reply(self, message_id: str, channel_id: str, content: str, token: str):
        header = {'Authorization': token, 'Content-Type': 'application/json'}
   
        while self.running:
            try:
                payload = {
                    "content": content,
                    "message_reference": {
                        "message_id": message_id,
                        "channel_id": channel_id
                    }
                }
           
                r = requests.post(
                    f'https://discord.com/api/v9/channels/{channel_id}/messages',
                    headers=header,
                    json=payload
                )
           
                if r.status_code == 200:
                    self.logger.success("SENT SUCCESSFULLY", token)
                elif r.status_code == 429:
                    self.logger.warning("RATE LIMIT", token)
                else:
                    self.logger.error("FAILED", token)
           
                time.sleep(0.01)
            except:
                continue

    def start(self):
        clear()
        print(ascii)
        print()
        
        if not self.tokens:  
            return
   
        channel_id = self.logger.input("CHANNEL ID")
        message_id = self.logger.input("MESSAGE ID")
        content = self.logger.input("MESSAGE")
        thread_count = int(self.logger.input("THREADS"))
   
        threads = []
        for token in self.tokens[:thread_count]:
            thread = threading.Thread(
                target=self.spam_reply,
                args=(message_id, channel_id, content, token)
            )
            thread.start()
            threads.append(thread)

        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.running = False
            for thread in threads:
                thread.join()
