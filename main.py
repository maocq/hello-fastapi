import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from dependency_injector.wiring import Provide, inject
from application.config.containers import Container
from domain.model.user.user import User
from domain.usecase.create_user_usecase import CreateUserUsecase

@asynccontextmanager
async def lifespan(app: FastAPI):
    container = Container()
    container.wire(modules=[__name__])
    await container.init_resources()
    yield
    await container.shutdown_resources()

app = FastAPI(lifespan=lifespan)


@app.get("/")
@inject
async def create_user(
        create_user: CreateUserUsecase = Depends(Provide[Container.create_user_use_case])):
    user = User(name="Foo")
    return await create_user.create(user)


@app.get("/ls")
async def ls():
    cmd = "ls"
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        return stdout.decode()
    if stderr:
        return stderr.decode()
