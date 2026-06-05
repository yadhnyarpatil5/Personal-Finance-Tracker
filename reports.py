def monthly_summary(expenses):
    total = sum(expense.amount for expense in expenses)
    print("\nMonthly Expense Summary")
    print("-" * 30)
    print(f"Total Expenses: ₹{total}")

def category_report(expenses):
    categories = {}

    for expense in expenses:
        categories[expense.category] = categories.get(
            expense.category, 0) + expense.amount

    print("\nCategory-wise Report")
    print("-" * 30)

    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")
