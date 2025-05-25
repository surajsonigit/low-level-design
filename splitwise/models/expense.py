from typing import List
from .split import Split
from .user import User
from enums.expense_split_type import ExpenseSplitType

class Expense:
    def __init__(
        self,
        expense_id: str,
        expense_amount: float,
        description: str,
        paid_by_user: User,
        split_type: ExpenseSplitType,
        split_details: List[Split],
    ):
        self.expense_id = expense_id
        self.expense_amount = expense_amount
        self.description = description
        self.paid_by_user = paid_by_user
        self.split_type = split_type
        self.split_details = list(split_details)  # copies the list
