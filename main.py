from fastapi import FastAPI

from domain.model.user.user import User
from domain.usecase.create_user_usecase import CreateUserUsecase

app = FastAPI()


@app.get("/")
async def root():
    user = User(name = "Foo")
    use_case = CreateUserUsecase()
    return use_case.create_user(user)
