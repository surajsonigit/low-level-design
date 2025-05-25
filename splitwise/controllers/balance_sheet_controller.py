from typing import List
from models.balance import Balance
from models.split import Split
from models.user import User
from models.user_expense_balance_sheet import UserExpenseBalanceSheet

class BalanceSheetController:
    def update_user_expense_balance_sheet(self, expense_paid_by: User, splits: List[Split], total_expense_amount: float) -> None:
        # update the total amount paid by the user who paid the expense
        paid_by_user_expense_sheet: UserExpenseBalanceSheet = expense_paid_by.get_user_expense_balance_sheet()
        paid_by_user_expense_sheet.set_total_payment(paid_by_user_expense_sheet.get_total_payment() + total_expense_amount)

        for split in splits:
            user_owe = split.get_user()
            owe_user_expense_sheet: UserExpenseBalanceSheet = user_owe.get_user_expense_balance_sheet()
            owe_amount = split.get_amount_owe()

            if expense_paid_by.get_user_id() == user_owe.get_user_id():
                paid_by_user_expense_sheet.set_total_your_expense(
                    paid_by_user_expense_sheet.get_total_your_expense() + owe_amount
                )
            else:
                # update the balance of the user who paid
                paid_by_user_expense_sheet.set_total_you_get_back(
                    paid_by_user_expense_sheet.get_total_you_get_back() + owe_amount
                )

                user_owe_balance = paid_by_user_expense_sheet.get_user_vs_balance().get(user_owe.get_user_id())
                if user_owe_balance is None:
                    user_owe_balance = Balance()
                    paid_by_user_expense_sheet.get_user_vs_balance()[user_owe.get_user_id()] = user_owe_balance

                user_owe_balance.set_amount_get_back(user_owe_balance.get_amount_get_back() + owe_amount)

                # update the balance sheet of the user who owes money
                owe_user_expense_sheet.set_total_you_owe(owe_user_expense_sheet.get_total_you_owe() + owe_amount)
                owe_user_expense_sheet.set_total_your_expense(owe_user_expense_sheet.get_total_your_expense() + owe_amount)

                user_paid_balance = owe_user_expense_sheet.get_user_vs_balance().get(expense_paid_by.get_user_id())
                if user_paid_balance is None:
                    user_paid_balance = Balance()
                    owe_user_expense_sheet.get_user_vs_balance()[expense_paid_by.get_user_id()] = user_paid_balance

                user_paid_balance.set_amount_owe(user_paid_balance.get_amount_owe() + owe_amount)

    def show_balance_sheet_of_user(self, user: User) -> None:
        print("---------------------------------------")
        print(f"Balance sheet of user : {user.get_user_id()}")

        user_expense_balance_sheet: UserExpenseBalanceSheet = user.get_user_expense_balance_sheet()

        print(f"TotalYourExpense: {user_expense_balance_sheet.get_total_your_expense()}")
        print(f"TotalGetBack: {user_expense_balance_sheet.get_total_you_get_back()}")
        print(f"TotalYourOwe: {user_expense_balance_sheet.get_total_you_owe()}")
        print(f"TotalPaymentMade: {user_expense_balance_sheet.get_total_payment()}")

        for user_id, balance in user_expense_balance_sheet.get_user_vs_balance().items():
            print(f"userID: {user_id} YouGetBack: {balance.get_amount_get_back()} YouOwe: {balance.get_amount_owe()}")

        print("---------------------------------------")