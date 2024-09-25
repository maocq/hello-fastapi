from domain.model.user.gateways.user_repository import UserRepository
from domain.model.user.user import User

class CreateUserUsecase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, user: User) -> User:
        return await self.user_repository.create_user(user)

