from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_verified: bool


class AddUser(BaseModel):
    name: str
    is_verified: bool = False
