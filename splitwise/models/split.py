from .user import User

class Split:
    def __init__(self, user: User, amount_owe: float):
        self.user = user
        self.amount_owe = amount_owe

    def get_user(self) -> User:
        return self.user

    def set_user(self, user: User) -> None:
        self.user = user

    def get_amount_owe(self) -> float:
        return self.amount_owe

    def set_amount_owe(self, amount_owe: float) -> None:
        self.amount_owe = amount_owe
