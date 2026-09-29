# ==========================================
# BANK ACCOUNT MANAGEMENT SYSTEM
# Python Day 1 - Day 10 Mini Project
# ==========================================

# Day 1 & Day 2: Variables and Input
name = input("Enter account holder name: ")
age = int(input("Enter age: "))
account_type = input("Enter account type (Savings/Current): ")

# Starting balance
balance = 0.0

# Day 7: List
transactions = []

# Day 8: Tuple
account_details = (name, age, account_type)

# Day 9: Set
services = {"Deposit", "Withdraw", "Balance Check"}

# Day 10: Dictionary
account = {
    "name": name,
    "age": age,
    "account_type": account_type,
    "balance": balance,
    "transactions": transactions
}


# Day 6: Function
def show_account():
    print("\n========== ACCOUNT DETAILS ==========")
    print("Name:", account["name"])
    print("Age:", account["age"])
    print("Account Type:", account["account_type"])
    print("Balance:", account["balance"])
    print("Transactions:", account["transactions"])


# Day 6: Deposit Function
def deposit_money():
    amount = float(input("Enter deposit amount: "))

    # Day 4: Conditional Statement
    if amount > 0:
        account["balance"] = account["balance"] + amount
        account["transactions"].append("Deposit: " + str(amount))
        print("Deposit successful!")
    else:
        print("Invalid amount!")


# Day 6: Withdraw Function
def withdraw_money():
    amount = float(input("Enter withdrawal amount: "))

    # Day 3: Operators + Day 4: Conditional
    if amount > 0 and amount <= account["balance"]:
        account["balance"] = account["balance"] - amount
        account["transactions"].append("Withdraw: " + str(amount))
        print("Withdrawal successful!")
    elif amount > account["balance"]:
        print("Insufficient balance!")
    else:
        print("Invalid amount!")


# Day 5: While Loop
while True:

    print("\n========== BANK MENU ==========")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Show Account Details")
    print("5. Show Services")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit_money()

    elif choice == "2":
        withdraw_money()

    elif choice == "3":
        print("\nCurrent Balance:", account["balance"])

    elif choice == "4":
        show_account()

    elif choice == "5":
        print("\nAvailable Services:")

        # Day 5: For Loop
        for service in services:
            print("-", service)

    elif choice == "6":
        print("\nThank you for using Bank Account Management System!")
        break

    else:
        print("Invalid choice!")


print("\n======================================")
print("Bank Account Management System Completed!")