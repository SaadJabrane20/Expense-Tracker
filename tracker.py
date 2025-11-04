import os
import pandas as pd
from datetime import datetime

incomes = []
expenses = []
def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n====Menu====")
    print("1. Add income")
    print("2. Add expense")
    print("3. View Transactions")
    print("4. Check Current Balance")
    print("5. Delete Transactions")
    print("6. Save Data")
    print("0. Exit")

def add_income(amount, category):
    income = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    incomes.append(income)
    print(f"Added {amount}$ to incomes!")   

def add_expense(amount, category):
    expense = {
        "amount" : amount,
        "category" : category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    print(f"Added {amount}$ to expenses!")

def view_transactions():
    print("\n=== Transactions ===")
    
    print("\nIncomes:")
    if incomes:
        for idx, income in enumerate(incomes, 1):
            print(f"{idx}. {income['date']} - {income['category']} : ${income['amount']:.2f}")
    else:
        print("No incomes yet.")

    print("\nExpenses:")
    if expenses:
        for idx, expense in enumerate(expenses, 1):
            print(f"{idx}. {expense['date']} - {expense['category']} : ${expense['amount']:.2f}")
    else:
        print("No expenses yet.")

    input("\nPress Enter to continue...")


def check_balance():
    total_income = sum(i['amount'] for i in incomes)
    total_expense = sum(e['amount'] for e in expenses)
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Current Balance: ${total_income - total_expense:.2f}")


def delete_transaction():
    print("\n=== Delete Transaction ===")
    transaction_type = input("Enter transaction type (income or expense): ").lower()

    if transaction_type == 'income':
        if not incomes:
            print("No incomes to delete.")
            return
        for idx, income in enumerate(incomes, 1):
            print(f"{idx}. {income['date']} - {income['category']} : ${income['amount']:.2f}")
        try:
            n = int(input("Enter transaction number to delete: "))
            if 1 <= n <= len(incomes):
                deleted = incomes.pop(n-1)
                print(f"Deleted income: {deleted['category']} - ${deleted['amount']:.2f}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input. Enter a number.")
    
    elif transaction_type == 'expense':
        if not expenses:
            print("No expenses to delete.")
            return
        for idx, expense in enumerate(expenses, 1):
            print(f"{idx}. {expense['date']} - {expense['category']} : ${expense['amount']:.2f}")
        try:
            n = int(input("Enter transaction number to delete: "))
            if 1 <= n <= len(expenses):
                deleted = expenses.pop(n-1)
                print(f"Deleted expense: {deleted['category']} - ${deleted['amount']:.2f}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input. Enter a number.")
    else:
        print("Invalid transaction type. Enter 'income' or 'expense'.")

def save_data(filename="transactions.xlsx"):
    all_transactions = []
    for i in incomes:
        all_transactions.append({"Type": "Income", **i})
    for e in expenses:
        all_transactions.append({"Type": "Expense", **e})

    if not all_transactions:
        print("No transactions to save.")
        return

    df = pd.DataFrame(all_transactions)

    try:
        df.to_excel(filename, index=False)
        print(f"Data successfully saved to {filename}!")
    except Exception as e:
        print(f"Error saving file: {e}")