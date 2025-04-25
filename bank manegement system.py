class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def get_balance(self):
        return self.balance
def main():
    account_holder_name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))

    # Creating a BankAccount object
    account = BankAccount(account_holder_name, initial_balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            deposit_amount = float(input("Enter deposit amount: "))
            account.deposit(deposit_amount)

        elif choice == '2':
            withdraw_amount = float(input("Enter withdrawal amount: "))
            account.withdraw(withdraw_amount)

        elif choice == '3':
            print(f"Current balance: ${account.get_balance()}")

        elif choice == '4':
            print("Exiting the bank management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
usar