from msgspec import Struct
from datetime import datetime

class BaseDTO(Struct):
    def to_dict(self):
        return {f: getattr(self, f) for f in self.__struct_fields__}

class UserDTO(BaseDTO):
    id: int
    name: str
    surname: str
    password: str
    created_at: datetime
    updated_at: datetime

class UserCreateDTO(BaseDTO):
    name: str
    surname: str
    password: str

class UserUpdateDTO(BaseDTO):
    name: str | None = None
    surname: str | None = None
    password: str | None = None


class UserReadDTO(BaseDTO):
    id: int
    name: str
    surname: str
    created_at: str
    updated_at: str

class UserDeleteDTO(BaseDTO):
    pass
