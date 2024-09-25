import aiohttp
from dependency_injector import containers, providers

from domain.usecase.create_user_usecase import CreateUserUsecase
from infrastructure.driven_adapter.httpclient.user_http_repository import UserHttpRepository

async def http_client_session(limit = 100):
    connector = aiohttp.TCPConnector(limit=limit)
    client_session = aiohttp.ClientSession(connector=connector)
    yield client_session
    await client_session.close()

class Container(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(modules=["main"])
    http_client = providers.Resource(http_client_session, limit=100)
    user_repository = providers.Factory(UserHttpRepository, http_client=http_client)
    create_user_use_case = providers.Factory(CreateUserUsecase, user_repository=user_repository)