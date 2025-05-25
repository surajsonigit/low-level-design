from abc import ABC, abstractmethod
from typing import List
from models.split import Split

class ExpenseSplit(ABC):
    @abstractmethod
    def validate_split_request(self, split_list: List[Split], total_amount: float) -> None:
        pass
