from fastapi import FastAPI

from domain.model.user.user import User
from domain.usecase.create_user_usecase import CreateUserUsecase
from infrastructure.driven_adapter.httpclient.user_http_repository import UserHttpRepository

app = FastAPI()

user_repository = UserHttpRepository()
create_user_use_case = CreateUserUsecase(user_repository)

@app.get("/")
async def root():
    user = User(name="Foo")
    return create_user_use_case.create_user(user)
