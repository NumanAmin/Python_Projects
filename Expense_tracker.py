import csv
from datetime import datetime

expenses = []


# Load Expenses From CSV
def load_expenses():

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:

                expense = {
                    "category": row[0],
                    "amount": int(row[1]),
                    "date": row[2],
                    "time": row[3]
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass


# Save Single Expense (Add)
def save_expense(category, amount):

    now = datetime.now()

    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([category, amount, date, time])


# Save All Expenses (Edit/Delete Fix)
def save_all_expenses():

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for expense in expenses:

            writer.writerow([
                expense["category"],
                expense["amount"],
                expense["date"],
                expense["time"]
            ])


# Add Expense
def add_expense():

    category = input("Enter Category: ")

    try:
        amount = int(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount!")
        return

    now = datetime.now()

    expense = {
        "category": category,
        "amount": amount,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    }

    expenses.append(expense)

    save_expense(category, amount)

    print("Expense Added Successfully!")


# View Expenses
def view_expenses():

    if len(expenses) == 0:
        print("No Expenses Found!")

    else:
        print("\nYour Expenses:")

        for i, expense in enumerate(expenses, start=1):

            print(
                i,
                "-",
                expense["category"],
                "- Rs.",
                expense["amount"],
                "-",
                expense["date"],
                expense["time"]
            )


# Total Expense
def total_expense():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense = Rs.", total)


# Delete Expense
def delete_expense():

    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    view_expenses()

    try:
        number = int(input("Enter Expense Number To Delete: "))
    except ValueError:
        print("Invalid Number!")
        return

    if 1 <= number <= len(expenses):

        del expenses[number - 1]

        save_all_expenses()

        print("Expense Deleted Successfully!")

    else:
        print("Invalid Expense Number!")


# Edit Expense
def edit_expense():

    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    view_expenses()

    try:
        number = int(input("Enter Expense Number To Edit: "))
        new_amount = int(input("Enter New Amount: "))
    except ValueError:
        print("Invalid Input!")
        return

    if 1 <= number <= len(expenses):

        new_category = input("Enter New Category: ")

        now = datetime.now()

        expenses[number - 1]["category"] = new_category
        expenses[number - 1]["amount"] = new_amount
        expenses[number - 1]["date"] = now.strftime("%Y-%m-%d")
        expenses[number - 1]["time"] = now.strftime("%H:%M:%S")

        save_all_expenses()

        print("Expense Updated Successfully!")

    else:
        print("Invalid Expense Number!")


# Program Start
load_expenses()


# Main Menu
while True:

    print("\n===== Advanced Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        edit_expense()

    elif choice == "6":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")