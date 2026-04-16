from fastapi import HTTPException

from internal.models.user_model import AddUser, User
from internal.services.user_service import UserService

service = UserService()


def create_user(user: AddUser) -> User:
    return service.create_user(user)


def read_user(user_id: int) -> User:
    try:
        return service.read_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def read_users() -> list[User]:
    return service.read_users()


def update_user(user_id: int, name: str) -> User:
    try:
        return service.update_user(user_id, name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


def delete_user(user_id: int) -> dict:
    try:
        service.delete_user(user_id)
        return {"message": "User deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
