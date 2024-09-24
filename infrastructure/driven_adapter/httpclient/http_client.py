import aiohttp

class HttpClient:
    def __init__(self, limit: int = 100):
        self.session: aiohttp.ClientSession | None = None
        self.limit = limit

    def connect(self):
        if self.session is None:
            connector = aiohttp.TCPConnector(limit=self.limit)
            self.session = aiohttp.ClientSession(connector=connector)

    async def close(self):
        await self.session.close()

http_client = HttpClient()
