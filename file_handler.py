import json

def save_expenses(expenses, filename="expenses.json"):
    data = [expense.to_dict() for expense in expenses]
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
