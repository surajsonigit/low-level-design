from typing import List
from models.split import Split
from .expense_split import ExpenseSplit

class PercentageExpenseSplit(ExpenseSplit):
    def validate_split_request(self, split_list: List[Split], total_amount: float) -> None:
        # Currently, no validation logic is provided.
        pass
