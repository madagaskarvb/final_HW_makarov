from fastapi import APIRouter

from internal.handlers import crud_handler
from internal.models.user_model import AddUser, User

router = APIRouter()


@router.get("/", response_model=list[User])
def get_users():
    return crud_handler.read_users()


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    return crud_handler.read_user(user_id)


@router.post("/create", response_model=User, status_code=201)
def post_user(user: AddUser):
    return crud_handler.create_user(user)


@router.put("/{user_id}", response_model=User)
def put_user(user_id: int, name: str):
    return crud_handler.update_user(user_id, name)


@router.delete("/{user_id}")
def remove_user(user_id: int):
    return crud_handler.delete_user(user_id)
