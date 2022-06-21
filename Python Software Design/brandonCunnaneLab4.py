"""
CS3B Lab 4: OOP
Brandon Cunnane
This program tests the Bank Account class.
"""

from brandonCunnaneBank import BankAccount


def main():
    account = BankAccount(1000.00)
    account.deposit(500.00)
    account.withdraw(2000.00)
    account.add_interest(0.01)
    account.add_interest(0.02)
    account.deposit(125000.99)
    account.withdraw(0.99)
    account.withdraw(126500.00)
    account.withdraw(10)
    account.add_interest(0.01)


if __name__ == '__main__':
    main()

"""
Account balance is $1,504.90

Action: Deposit $125,000.99
Account balance is $126,505.89

Action: Withdraw $0.99
Account balance is $126,504.90

Action: Withdraw $126,500.00
Account balance is $4.90

Action: Withdraw $10.00
Insufficient funds available for withdrawal. Overdraft fee of $10 applied.
Account balance is -$5.10

Action: Add interest at rate of 1.00%
Negative balances cannot accrue interest.
Account balance is -$5.10
"""