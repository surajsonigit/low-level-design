from typing import List, Optional
from models.user import User

class UserController:
    def __init__(self):
        self.user_list: List[User] = []

    # Add user
    def add_user(self, user: User) -> None:
        self.user_list.append(user)

    def get_user(self, user_id: str) -> Optional[User]:
        for user in self.user_list:
            if user.get_user_id() == user_id:
                return user
        return None

    def get_all_users(self) -> List[User]:
        return self.user_list
