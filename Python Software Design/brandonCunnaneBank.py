"""
CS3B Lab 4: OOP
Brandon Cunnane
This program implements the Bank Account class.
"""

import decimal as dec
from datetime import date

class BankAccount:
    OVERDRAFT_FEE = dec.Decimal(10.00)
    RATE_MAX = 0.02
    RATE_MIN = 0.01

    def __init__(self, initial_balance=dec.Decimal(0.0), initial_interest_date=date(2021, 1, 1)):
        initial_balance = dec.Decimal(initial_balance)
        self.balance = initial_balance
        self.last_interest_date = initial_interest_date
        print(str(self))

    def __str__(self):
        if self.get_balance() > 0:
            return f"Account balance is ${self.get_balance():,.2f}\n"
        elif self.get_balance() < 0:
            return f"Account balance is -${abs(self.get_balance()):,.2f}\n"

    def set_balance(self, new_balance):
        if not isinstance(new_balance, dec.Decimal):
            print("Balances must be decimal numbers.")
        self.balance = new_balance

    def get_balance(self):
        return self.balance

    def set_last_interest_date(self, new_date):
        self.last_interest_date = new_date

    def get_last_interest_date(self):
        return self.last_interest_date

    def deposit(self, amount):
        amount = dec.Decimal(amount)
        new_balance = self.get_balance() + amount
        self.set_balance(new_balance)
        print(f"Action: Deposit ${amount:,.2f}")
        print(str(self))

    def withdraw(self, amount):
        amount = dec.Decimal(amount)
        print(f"Action: Withdraw ${amount:,.2f}")
        if self.get_balance() - amount < 0:
            print(f"Insufficient funds available for withdrawal. "
                  f"Overdraft fee of ${BankAccount.OVERDRAFT_FEE} applied.")
            new_balance = self.get_balance() - BankAccount.OVERDRAFT_FEE
        else:
            new_balance = self.get_balance() - amount
        self.set_balance(new_balance)
        print(str(self))

    def add_interest(self, rate):
        print(f"Action: Add interest at rate of {rate * 100:.2f}%")
        days_since_interest = date.today() - self.get_last_interest_date()
        if self.get_balance() < 0:
            print("Negative balances cannot accrue interest.")
        elif not BankAccount.RATE_MIN <= rate <= BankAccount.RATE_MAX:
            print(f"Invalid interest rate. "
                  f"Must be between {BankAccount.RATE_MIN} and "
                  f"{BankAccount.RATE_MAX}")
        elif days_since_interest.days < 30:
            print(f"Interest is applied once monthly every 30 days or more. "
                  f"It has been {days_since_interest.days} days since "
                  f"interest was applied.")
        elif days_since_interest.days >= 30:
            rate = dec.Decimal(rate)
            new_balance = self.get_balance() * (1 + rate)
            self.set_balance(new_balance)
            self.set_last_interest_date(date.today())
        print(str(self))
