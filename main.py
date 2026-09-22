class BankAccount:

    def __init__(self, name, account_number, pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = 0
        self.transactions = []

    # Deposit money
    def deposit(self, amount):

        if amount <= 0:
            print("❌ Amount must be greater than 0")
            return

        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")

        print(f"✅ ₹{amount} deposited successfully")
        print(f"💰 Current Balance: ₹{self.balance}")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("❌ Amount must be greater than 0")
            return

        if amount > self.balance:
            print("❌ Insufficient balance")
            return

        self.balance -= amount
        self.transactions.append(f"Withdrawn ₹{amount}")

        print(f"✅ ₹{amount} withdrawn successfully")
        print(f"💰 Current Balance: ₹{self.balance}")

    # Check balance
    def check_balance(self):

        print("\n-------------------------")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance       : ₹{self.balance}")
        print("-------------------------")

    # Transaction history
    def show_transactions(self):

        print("\n===== TRANSACTION HISTORY =====")

        if len(self.transactions) == 0:
            print("No transactions yet.")
            return

        for transaction in self.transactions:
            print("•", transaction)


# Store all accounts
accounts = {}


# Create account
def create_account():

    print("\n===== CREATE ACCOUNT =====")

    name = input("Enter your name: ")
    account_number = input("Enter account number: ")
    pin = input("Create 4-digit PIN: ")

    if account_number in accounts:
        print("❌ Account already exists")
        return

    if len(pin) != 4 or not pin.isdigit():
        print("❌ PIN must contain exactly 4 digits")
        return

    account = BankAccount(name, account_number, pin)

    accounts[account_number] = account

    print("\n✅ Account created successfully!")
    print(f"Welcome, {name}!")


# Login
def login():

    print("\n===== LOGIN =====")

    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number not in accounts:
        print("❌ Account not found")
        return None

    account = accounts[account_number]

    if account.pin != pin:
        print("❌ Incorrect PIN")
        return None

    print(f"\n✅ Welcome back, {account.name}!")

    return account


# User dashboard
def dashboard(account):

    while True:

        print("\n========== BANK MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Logout")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            account.check_balance()

        elif choice == "2":

            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

            except ValueError:
                print("❌ Please enter a valid amount")

        elif choice == "3":

            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

            except ValueError:
                print("❌ Please enter a valid amount")

        elif choice == "4":

            account.show_transactions()

        elif choice == "5":

            print("👋 Logged out successfully")
            break

        else:

            print("❌ Invalid choice")


# Main program
def main():

    while True:

        print("\n")
        print("================================")
        print("       🏦 PYTHON BANK")
        print("================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            create_account()

        elif choice == "2":

            account = login()

            if account:
                dashboard(account)

        elif choice == "3":

            print("\nThank you for using Python Bank! 👋")
            break

        else:

            print("❌ Invalid choice")


main()