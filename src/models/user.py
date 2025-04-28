from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseModel
from src.utils.custom_types import created_at, updated_at


class UserModel(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }   
