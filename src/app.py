from litestar import Litestar
from litestar.plugins.sqlalchemy import (
    SQLAlchemyInitPlugin,
    SQLAlchemySerializationPlugin,
)
from src.api.user_api import UserController
from src.database.session import sqlalchemy_config
from src.models.base import BaseModel


# async def on_startup() -> None:
#     async with sqlalchemy_config.get_engine().begin() as conn:
#         await conn.run_sync(BaseModel.metadata.create_all)


app = Litestar(
    route_handlers=[UserController],
    # on_startup=[on_startup],
    plugins=[
        SQLAlchemyInitPlugin(config=sqlalchemy_config),
        SQLAlchemySerializationPlugin(),
    ],
    # debug=True,
)
