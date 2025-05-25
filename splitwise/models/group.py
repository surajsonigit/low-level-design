from typing import List
from .user import User
from .expense import Expense
from controllers.expense_controller import ExpenseController
from enums.expense_split_type import ExpenseSplitType
from .split import Split

class Group:
    def __init__(self):
        self.group_id: str = ""
        self.group_name: str = ""
        self.group_members: List[User] = []
        self.expense_list: List[Expense] = []
        self.expense_controller = ExpenseController()

    def add_member(self, member: User) -> None:
        self.group_members.append(member)

    def get_group_id(self) -> str:
        return self.group_id

    def set_group_id(self, group_id: str) -> None:
        self.group_id = group_id

    def set_group_name(self, group_name: str) -> None:
        self.group_name = group_name

    def create_expense(
        self,
        expense_id: str,
        description: str,
        expense_amount: float,
        split_details: List[Split],
        split_type: ExpenseSplitType,
        paid_by_user: User,
    ) -> Expense:
        expense = self.expense_controller.create_expense(
            expense_id, description, expense_amount, split_details, split_type, paid_by_user
        )
        self.expense_list.append(expense)
        return expense
