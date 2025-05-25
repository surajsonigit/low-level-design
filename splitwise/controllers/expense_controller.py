from typing import List
from .balance_sheet_controller import BalanceSheetController
from models.split import Split
from models.expense import Expense
from services.expense.expense_split import ExpenseSplit
from services.split_factory import SplitFactory
from enums.expense_split_type import ExpenseSplitType
from models.user import User

class ExpenseController:
    def __init__(self):
        self.balance_sheet_controller = BalanceSheetController()

    def create_expense(
        self,
        expense_id: str,
        description: str,
        expense_amount: float,
        split_details: List[Split],
        split_type: ExpenseSplitType,
        paid_by_user: User,
    ) -> Expense:
        expense_split: ExpenseSplit = SplitFactory.get_split_object(split_type)
        expense_split.validate_split_request(split_details, expense_amount)

        expense = Expense(expense_id, expense_amount, description, paid_by_user, split_type, split_details)

        self.balance_sheet_controller.update_user_expense_balance_sheet(paid_by_user, split_details, expense_amount)

        return expense
