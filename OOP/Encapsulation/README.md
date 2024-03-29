### Tutotrial video can be found here: https://youtu.be/xsW6Lm8fSvU?si=7qWrk-EEt8lN2t9H
# Bank Account Class with Protected and Private Attributes

## Overview

This code demonstrates the implementation of a `BankAccount` class in Python, showcasing the use of protected and private attributes to encapsulate sensitive information. The class provides methods for depositing and withdrawing funds, as well as a getter method to retrieve the account balance.

## Understanding Protected and Private Attributes

In Python, attributes can be declared as protected or private to control their accessibility and protect sensitive data. Protected attributes are accessible within the class and its subclasses, while private attributes are only accessible within the class itself.

## Implementation Details

### 1. Class Definition

```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = balance  # Private attribute
```

- The `BankAccount` class is defined with two attributes: `_account_holder` (protected) and `__balance` (private).
- The `__init__` method initializes the account with an `account_holder` and an optional `balance` (default is 0).

### 2. Deposit Method

```python
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
```

- The `deposit` method allows users to deposit funds into the account.
- It checks if the `amount` is greater than 0 and adds it to the `__balance` if valid.
- A success message is printed, displaying the deposited amount and the updated balance.

### 3. Withdraw Method

```python
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
```

- The `withdraw` method enables users to withdraw funds from the account.
- It checks if the `amount` is greater than 0 and less than or equal to the current balance.
- If valid, the amount is subtracted from the `__balance`, and a success message is displayed.

### 4. Get Balance Method

```python

def get_balance(self):
        return self.__balance
```
- The 'get_balance' method enables users to check funds remmaining in their account.
