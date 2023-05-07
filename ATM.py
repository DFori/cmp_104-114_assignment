class Account:
    def __init__(self):
        self.name = "Daniel Fori"
        self.account_number = 7944576116
        self.account_balance = 1000000

    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance)

    def withdraw(self, amount):
        self.account_balance -= amount
        print(self.account_balance)

    def check_balance(self):
        print(self.account_balance)