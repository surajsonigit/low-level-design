from .expense.equal_expense_split import EqualExpenseSplit
from .expense.unequal_expense_split import UnequalExpenseSplit
from .expense.percentage_expense_split import PercentageExpenseSplit
from .expense.expense_split import ExpenseSplit
from enums.expense_split_type import ExpenseSplitType

class SplitFactory:
    @staticmethod #imp
    def get_split_object(split_type: ExpenseSplitType) -> ExpenseSplit:
        if split_type == ExpenseSplitType.EQUAL:
            return EqualExpenseSplit()
        elif split_type == ExpenseSplitType.UNEQUAL:
            return UnequalExpenseSplit()
        elif split_type == ExpenseSplitType.PERCENTAGE:
            return PercentageExpenseSplit()
        else:
            return None
