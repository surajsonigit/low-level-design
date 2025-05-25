from typing import List
from models.user import User
from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from models.split import Split
from enums.expense_split_type import ExpenseSplitType
from controllers.balance_sheet_controller import BalanceSheetController

class Splitwise:
    def __init__(self):
        self.user_controller = UserController()
        self.group_controller = GroupController()
        self.balance_sheet_controller = BalanceSheetController()

    def demo(self) -> None:
        self.setup_user_and_group()

        # add new users to the group
        group = self.group_controller.get_group("G1001")
        group.add_member(self.user_controller.get_user("U2001"))
        group.add_member(self.user_controller.get_user("U3001"))

        # create an expense inside a group
        splits: List[Split] = [
            Split(self.user_controller.get_user("U1001"), 300),
            Split(self.user_controller.get_user("U2001"), 300),
            Split(self.user_controller.get_user("U3001"), 300)
        ]
        group.create_expense("Exp1001", "Breakfast", 900, splits, ExpenseSplitType.EQUAL, self.user_controller.get_user("U1001"))

        splits2: List[Split] = [
            Split(self.user_controller.get_user("U1001"), 400),
            Split(self.user_controller.get_user("U2001"), 100)
        ]
        group.create_expense("Exp1002", "Lunch", 500, splits2, ExpenseSplitType.UNEQUAL, self.user_controller.get_user("U2001"))

        for user in self.user_controller.get_all_users():
            self.balance_sheet_controller.show_balance_sheet_of_user(user)

    def setup_user_and_group(self) -> None:
        # add new user to splitwise app
        self.add_users_to_splitwise_app()

        # create a group by user1
        user1 = self.user_controller.get_user("U1001")
        self.group_controller.create_new_group("G1001", "Outing with Friends", user1)

    def add_users_to_splitwise_app(self) -> None:
        # adding User1
        user1 = User("U1001", "User1")

        # adding User2
        user2 = User("U2001", "User2")

        # adding User3
        user3 = User("U3001", "User3")

        self.user_controller.add_user(user1)
        self.user_controller.add_user(user2)
        self.user_controller.add_user(user3)
