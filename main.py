import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from domain.model.user.user import User
from domain.usecase.create_user_usecase import CreateUserUsecase
from infrastructure.driven_adapter.httpclient.http_client import http_client
from infrastructure.driven_adapter.httpclient.user_http_repository import UserHttpRepository

@asynccontextmanager
async def lifespan(app: FastAPI):
    http_client.connect()
    yield
    await http_client.close()

app = FastAPI(lifespan=lifespan)

user_repository = UserHttpRepository()
create_user_use_case = CreateUserUsecase(user_repository)

@app.get("/")
async def root():
    user = User(name="Foo")
    return await create_user_use_case.create_user(user)


@app.get("/ls")
async def rootls():
    cmd = "ls"
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
        return stdout.decode()
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
        return stderr.decode()