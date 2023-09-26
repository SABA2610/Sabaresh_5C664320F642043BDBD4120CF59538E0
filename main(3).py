class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposit successful. New balance:", self.__account_balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdrawal successful. New balance:", self.__account_balance)
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print("Account balance:", self.__account_balance)


# Test the BankAccount class
account = BankAccount("12345", "John Doe", 1000)
account.display_balance()

account.deposit(500)
account.withdraw(200)
account.display_balance()