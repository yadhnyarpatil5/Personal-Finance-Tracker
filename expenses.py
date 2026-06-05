from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
    
class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)

    def view_expenses(self):
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense.date} | ₹{expense.amount} | "
                  f"{expense.category} | {expense.description}")
