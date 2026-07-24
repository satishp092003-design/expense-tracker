import json
import os
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    while True:
        amount_input = input("Amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Please enter a valid number for amount.\n")

    category = input("Category (e.g. Food, Travel, Rent): ").strip()
    if not category:
        category = "Uncategorized"

    note = input("Note (optional): ")
    entry = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": str(date.today())
    }
    expenses.append(entry)
    save_expenses(expenses)
    print("Expense added.\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\nAll Expenses:")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")
    print()


def show_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    totals = {}
    for e in expenses:
        totals[e['category']] = totals.get(e['category'], 0) + e['amount']

    print("\nSummary by Category:")
    for category, total in totals.items():
        print(f"{category}: ₹{total}")
    grand_total = sum(totals.values())
    print(f"Total spent: ₹{grand_total}\n")    


def main():
    expenses = load_expenses()
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Summary by category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()
