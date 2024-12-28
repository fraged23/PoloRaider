from core.utils.init import *
from core.utils.logging import Logger

class Spammer:
    def __init__(self):
        self.theme = theme
        self.tokens = self.load_tokens()
        self.headers = {
            'Authorization': None,
            'Content-Type': 'application/json'
        }
        self.logger = Logger(theme)
        
    def load_tokens(self):
        with open('data/input/tokens.txt', 'r') as f:
            return [token.strip() for token in f.readlines() if token.strip()]

    async def spam(self, channel_id, message, token):
        headers = self.headers.copy()
        headers['Authorization'] = token
        payload = {'content': message}
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    f'https://discord.com/api/v9/channels/{channel_id}/messages',
                    headers=headers,
                    json=payload
                ) as r:
                    if r.status == 200:
                        self.logger.success("SENT SUCCESSFULLY", token)
                    elif r.status == 401:
                        self.logger.error("INVALID TOKEN", token)
                    else:
                        self.logger.error("FAILED", token)
            except Exception:
                self.logger.error("FAILED", token)

    async def spam_all(self, channel_id, message, thread_count):
        while True:
            for i in range(0, len(self.tokens), thread_count):
                batch = self.tokens[i:i + thread_count]
                tasks = [self.spam(channel_id, message, token) for token in batch]
                await asyncio.gather(*tasks)
                await asyncio.sleep(0.01)

    def start(self):
        clear()
        print(ascii)
        print()
        
        channel_id = self.logger.input("CHANNEL ID")
        message = self.logger.input("MESSAGE")
        threads = int(self.logger.input("THREADS"))

        if not self.tokens:
            clear()
            print(ascii)
            print()
            self.logger.error("Couldn't find any tokens, Returning.")
            self.logger.input("Press Enter")
            return

        asyncio.run(self.spam_all(channel_id, message, threads))
