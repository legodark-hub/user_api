from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from advanced_alchemy.base import BigIntAuditBase


class UserModel(BigIntAuditBase):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }   
