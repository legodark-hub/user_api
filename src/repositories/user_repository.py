from litestar.plugins.sqlalchemy import repository
from src.models.user import UserModel
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(repository.SQLAlchemyAsyncRepository[UserModel]):
    model_type = UserModel
    

async def provide_user_repository(db_session: AsyncSession) -> UserRepository:
    return UserRepository(session=db_session)