from argparse import ArgumentError
import csv
import os.path


class Bank:
    pass


class Account:
    def __init__(self, id, balance, open_date):
        if int(balance) < 0:
            raise Exception(
                "Sorry, an account cannot be created with negative funds.")
        self.id = int(id)
        self.balance = balance
        self.open_date = open_date

    @classmethod
    def all_accounts(cls):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        fieldnames = ['id', 'balance', 'open_date']
        with open(path) as csvfile:
            accounts_reader = csv.DictReader(csvfile, fieldnames)
            for row in accounts_reader:
                accounts.append(Account(**dict(row)))
        return accounts

    @classmethod
    def find(cls, id):
        print(id)
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        fieldnames = ['id','balance','open_date']
        with open(path) as csvfile:
            accounts_reader = csv.DictReader(csvfile, fieldnames)
            for row in accounts_reader:
                if int(row['id']) == id:
                    print(row)
                    accounts.append(Account(**dict(row)))
        return accounts

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print(
                f"You have not enough funds to complete the transaction. Your current balance is ${self.balance}")
        else:
            self.  balance -= withdraw_amount
        return self.balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance

    def owner(self, owner):
        self.owner = owner


class Owner:
    def __init__(self, id, last_name, first_name, street_address, city, state):
        self.id = int(id)
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state


class SavingsAccount(Account):
    def __init__(self, id, balance, open_date):
        super().__init__(id, balance, open_date)
        if balance < 10:
            raise ValueError("Initial balance cannot be less than $10")

    def add_interest(self, rate = 0.25):
        interest = self.balance * rate / 100
        self.balance += interest
        return interest

    def withdraw(self, withdraw_amount):
        new_balance = self.balance - withdraw_amount

        if new_balance < 10:
            print(f"You have not enough funds to complete this transaction. Your current balance is ${self.balance}")
        else:
            self.balance = new_balance + 2
        return self.balance


class CheckingAccount(Account):
    def __init__(self, id, balance, open_date):
        super().__init__(id, balance, open_date)
        self.check_count = 0

    def withdraw(self, withdraw_amount):
        if self.balance - (withdraw_amount + 1) < 0:
            print(f"You have not enough funds to complete this transaction. Your current balance is ${self.balance}")
        else:
            self.balance -= (withdraw_amount + 1)
            return self.balance
        
    def withdraw_using_check(self, withdraw_amount):
        if self.balance - withdraw_amount < -10:
            print(f"You have not enough funds to complete this transaction. Your current balance is ${self.balance}")
        if self.check_count >= 3:
            self.balance -= (withdraw_amount + 2)
            return self.balance
        else:
            self.balance -= withdraw_amount
            self.check_count += 1
            print(self.check_count)
            return self.balance
    
    def reset_checks(self):
        self.check_count = 0


x = CheckingAccount(1212,100,"1999-03-27 11:30:09 -0800")
print (x.withdraw_using_check(60))
print (x.withdraw_using_check(10))
print (x.withdraw_using_check(10))
print (x.withdraw_using_check(10))