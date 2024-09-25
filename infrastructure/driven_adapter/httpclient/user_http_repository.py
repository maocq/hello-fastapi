import aiohttp

from domain.model.user.gateways.user_repository import UserRepository
from domain.model.user.user import User

class UserHttpRepository(UserRepository):
    def __init__(self, http_client: aiohttp.ClientSession):
        self._client = http_client

    async def create_user(self, user: User) -> User:
        async with self._client.get("http://localhost:3000/10") as response:
            return await response.json()