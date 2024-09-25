from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.config.containers import Container
from infrastructure.entry_points.rest import rest_controller


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = Container()
    container.wire(modules=[rest_controller.__name__])
    await container.init_resources()
    yield
    await container.shutdown_resources()


def start() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(rest_controller.router)
    return app