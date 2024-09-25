import asyncio

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from application.config.containers import Container
from domain.model.user.user import User
from domain.usecase.create_user_usecase import CreateUserUsecase

router = APIRouter()

@router.get("/")
@inject
async def create_user(
        create_user_use_case: CreateUserUsecase = Depends(Provide[Container.create_user_use_case])):
    user = User(name="Foo")
    return await create_user_use_case.create(user)


@router.get("/ls")
async def ls():
    cmd = "ls"
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        return stdout.decode()
    if stderr:
        return stderr.decode()