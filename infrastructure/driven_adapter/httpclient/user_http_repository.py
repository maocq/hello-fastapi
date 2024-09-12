from domain.model.user.gateways.user_repository import UserRepository
from domain.model.user.user import User

class UserHttpRepository(UserRepository):
    def create_user(self, user: User) -> User:
        return user