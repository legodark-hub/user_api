from litestar import Controller, patch, post, get, delete
from litestar.di import Provide
import msgspec
from src.models.user import UserModel
from src.repositories.user_repository import UserRepository, provide_user_repository
from src.schemas.user_dto import UserCreateDTO, UserDTO, UserReadDTO, UserUpdateDTO


class UserController(Controller):
    path = "/users"
    dependencies = {"user_repo": Provide(provide_user_repository)}

    @post("/")
    async def create_user(self, data: UserCreateDTO, user_repo: UserRepository) -> UserReadDTO:
        user = await user_repo.add(UserModel(**data.to_dict()))
        await user_repo.session.commit()
        return UserReadDTO(**user.to_dict())

    @get("/")
    async def list_users(self, user_repo: UserRepository) -> list[UserReadDTO]:
        users = await user_repo.list()
        return [UserReadDTO(**user.to_dict()) for user in users]

    @get("/{user_id:int}")
    async def get_user(self, user_id: int, user_repo: UserRepository) -> UserReadDTO | None:
        user = await user_repo.get(user_id)
        return UserReadDTO(**user.to_dict()) if user else None

    @patch("/{user_id:int}")
    async def update_user(self, user_id: int, data: UserUpdateDTO, user_repo: UserRepository) -> UserReadDTO | None:
        dict = data.to_dict()
        dict.update({"id": user_id})
        user = await user_repo.update(UserModel(**dict))
        await user_repo.session.commit()
        return UserReadDTO(**user.to_dict()) if user else None

    @delete("/{user_id:int}")
    async def delete_user(self, user_id: int, user_repo: UserRepository) -> None:
        _ = await user_repo.delete(user_id)
        await user_repo.session.commit()
        
