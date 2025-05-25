from typing import List
from models.split import Split
from .expense_split import ExpenseSplit

class EqualExpenseSplit(ExpenseSplit):
    def validate_split_request(self, split_list: List[Split], total_amount: float) -> None:
        if not split_list:
            raise ValueError("Split list cannot be empty.")
        
        amount_should_be_present = total_amount / len(split_list)
        for split in split_list:
            if split.get_amount_owe() != amount_should_be_present:
                raise ValueError(f"Split amount for user {split.get_user().get_user_id()} is incorrect. Expected: {amount_should_be_present}, Got: {split.get_amount_owe()}")
