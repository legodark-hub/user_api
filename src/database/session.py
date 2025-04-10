from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyInitPlugin,
    SQLAlchemyAsyncConfig,
)

from src.config import DB_URL


session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=DB_URL, session_config=session_config
)
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)
