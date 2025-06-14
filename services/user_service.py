from typing import List, Optional
from schemas.models import User, UserCreate

class UserService:
    def __init__(self):
        self.users: List[User] = []
        self._next_id = 1

    def create_user(self, user: UserCreate) -> User:
        new_user = User(
            id=self._next_id,
            name=user.name,
            email=user.email,
            is_active=True
        )
        self.users.append(new_user)
        self._next_id += 1
        return new_user

    def get_user(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def get_all_users(self) -> List[User]:
        return self.users

    def update_user(self, user_id: int, user_data: UserCreate) -> Optional[User]:
        user = self.get_user(user_id)
        if user:
            user.name = user_data.name
            user.email = user_data.email
        return user

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            return True
        return False

    def deactivate_user(self, user_id: int) -> Optional[User]:
        user = self.get_user(user_id)
        if user:
            user.is_active = False
        return user

    def get_active_users(self) -> List[User]:
        return [user for user in self.users if user.is_active] 