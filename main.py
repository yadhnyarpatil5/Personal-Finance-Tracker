from expenses import Expense, ExpenseManager
from file_handler import save_expenses
from reports import monthly_summary, category_report

manager = ExpenseManager()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Category Report")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = Expense(date, amount, category, description)
        manager.add_expense(expense)

        print("Expense Added Successfully!")

    elif choice == "2":
        manager.view_expenses()

    elif choice == "3":
        monthly_summary(manager.expenses)

    elif choice == "4":
        category_report(manager.expenses)

    elif choice == "5":
        save_expenses(manager.expenses)
        print("Data Saved Successfully!")

    elif choice == "6":
        print("Thank You for Using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")
