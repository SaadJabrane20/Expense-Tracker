import os
incomes = []
expenses = []
def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n====Menu====")
    print("1. Add income")
    print("2. Add expense")
    print("4. View Transactions")
    print("5. Check Current Balance")
    print("6. Delete Transactions")
    print("7. Save Data")
    print("0. Exit")

def add_income(amount, category):
    income = {
        "amount": amount,
        "cateory": category
    }

    incomes.append(income)
    print(f"Added {amount} to incomes!")

def add_expense(amount, category):
    expense = {
        "amount" : amount,
        "category" : category
    }
    expenses.append(expense)
    print(f"Added {amount} to expenses!")
