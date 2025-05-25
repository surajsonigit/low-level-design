class Balance:
    def __init__(self):
        self.amount_owe: float = 0.0
        self.amount_get_back: float = 0.0

    def get_amount_owe(self) -> float:
        return self.amount_owe

    def set_amount_owe(self, amount_owe: float) -> None:
        self.amount_owe = amount_owe

    def get_amount_get_back(self) -> float:
        return self.amount_get_back

    def set_amount_get_back(self, amount_get_back: float) -> None:
        self.amount_get_back = amount_get_back
