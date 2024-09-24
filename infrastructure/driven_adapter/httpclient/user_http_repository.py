from domain.model.user.gateways.user_repository import UserRepository
from domain.model.user.user import User
from infrastructure.driven_adapter.httpclient.http_client import http_client

class UserHttpRepository(UserRepository):

    async def create_user(self, user: User) -> User:
        async with http_client.session.get("http://localhost:3000/10") as response:
            return await response.json()