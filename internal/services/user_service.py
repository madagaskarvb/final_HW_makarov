from internal.models.user_model import User, AddUser
from internal.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self._repo = UserRepository.get_instance()

    def create_user(self, user: AddUser) -> User:
        return self._repo.create_user(user)

    def read_user(self, user_id: int) -> User:
        user = self._repo.read_user(user_id)
        if user is None:
            raise ValueError(f"User with id {user_id} not found")
        return user

    def read_users(self) -> list[User]:
        return self._repo.read_users()

    def update_user(self, user_id: int, name: str) -> User:
        user = self._repo.update_user_name(user_id, name)
        if user is None:
            raise ValueError(f"User with id {user_id} not found")
        return user

    def delete_user(self, user_id: int) -> None:
        deleted = self._repo.delete_user(user_id)
        if not deleted:
            raise ValueError(f"User with id {user_id} not found")
