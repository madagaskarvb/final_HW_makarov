from internal.models.user_model import User, AddUser


class UserRepository:
    _instance: "UserRepository | None" = None

    def __init__(self):
        self._users: list[User] = []
        self._id_counter: int = 0

    @classmethod
    def get_instance(cls) -> "UserRepository":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_user(self, user: AddUser) -> User:
        self._id_counter += 1
        new_user = User(id=self._id_counter, name=user.name, is_verified=user.is_verified)
        self._users.append(new_user)
        return new_user

    def read_user(self, user_id: int) -> User | None:
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def read_users(self) -> list[User]:
        return list(self._users)

    def update_user_name(self, user_id: int, name: str) -> User | None:
        for i, user in enumerate(self._users):
            if user.id == user_id:
                self._users[i] = user.model_copy(update={"name": name})
                return self._users[i]
        return None

    def delete_user(self, user_id: int) -> bool:
        for i, user in enumerate(self._users):
            if user.id == user_id:
                self._users.pop(i)
                return True
        return False
