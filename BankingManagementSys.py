class BankAccount:
    def __init__(self, account_number, account_holder):
        """
        Constructor to initialize account number, account holder, and balance.
        Private attributes are used for encapsulation.
        """
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = 0

    def deposit(self, amount):
        """
        Method to deposit an amount into the bank account.
        The amount must be positive.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        """
        Method to withdraw an amount from the bank account.
        The amount must be positive and less than or equal to the current balance.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        """
        Method to get the current balance of the bank account.
        """
        return self.__balance

    def get_account_info(self):
        """
        Method to get the account information including account number, account holder, and balance.
        """
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: {self.__balance}"

# Function to create a new bank account using user input
def create_account():
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    return BankAccount(account_number, account_holder)

# Function to handle deposits with user input
def handle_deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account.deposit(amount)

# Function to handle withdrawals with user input
def handle_withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    account.withdraw(amount)

# Function to print account information
def print_account_info(account):
    print(account.get_account_info())

# Main function to interact with the user
def main():
    account = create_account()
    while True:
        print("\nChoose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Get account info")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            handle_deposit(account)
        elif choice == "2":
            handle_withdraw(account)
        elif choice == "3":
            print(f"Current balance: {account.get_balance()}")
        elif choice == "4":
            print_account_info(account)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()


