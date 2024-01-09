class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = balance  # Private attribute

    # Method to handle deposits
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Method to handle withdrawals
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Method to get the current balance
    def get_balance(self):
        return self.__balance


# Example Usage
account = BankAccount("Alice", 1000)

# Attempting to access protected and private attributes directly
# Accessing protected attribute
print(f"Account holder: {account._account_holder}")
# print(f"Balance: {account.__balance}")  # This line would raise an AttributeError

# Performing transactions using methods
account.deposit(500)
account.withdraw(200)

# Accessing the balance using a getter method
print(f"{account._account_holder}'s remaining balance: ${account.get_balance()}")
