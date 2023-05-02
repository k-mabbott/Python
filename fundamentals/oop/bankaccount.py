

# ------------------------------------------Bank class----------------
class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    
    def display_account_info(self):
        print(f"Balance is :{self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0: 
            self.balance *= (1 + self.int_rate) 
        else: 
            print("Insufficient funds to yield interest")
        return self

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Balance is: {account.balance} Interest rate: {account.int_rate}")

# --------------------------------------------User class------------

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(0.02, 100)
        self.saving = BankAccount(0.02)

    def what_account(account):
        if account == 'checking':
            acc = 'checking'
        if account == 'saving':
            acc = 'saving'
        return acc


    def make_deposit(self, amount, account):
        # User.what_account(account)
        # self.acc.deposit(amount)
        if account == 'checking':
            self.checking.deposit(amount)
        if account == 'saving':
            self.saving.deposit(amount)
        return self

    def make_withdrawal(self, amount, account):
        if account == 'checking':
            self.checking.withdraw(amount)
        if account == 'saving':
            self.saving.withdraw(amount)
        # print(self.account.balance)
        return self

    def display_user_balance(self):
        print(f"{self.name} Checking: ")
        self.checking.display_account_info()
        print(f"{self.name} Savings: ")
        self.saving.display_account_info()
        return self

    def transfer_money(self, amount, account, other_user, other_user_account):
        if account == 'checking':
            self.checking.withdraw(amount)
        elif account == 'saving':
            self.saving.withdraw(amount)
        else: 
            print("Check account type")
        if other_user_account == 'checking':
            other_user.checking.deposit(amount)
        elif other_user_account == 'saving':
            self.saving.deposit(amount)
        else: 
            print("Check account type")
        return self
        




user_kyle = User('Kyle', 'fake@email.com')
user_kyle.make_deposit(100, 'checking').make_withdrawal(20, 'checking').display_user_balance()
user_other = User('Guy', 'not@an.email')
user_other.make_deposit(100, 'checking').transfer_money(25, 'checking', user_kyle, 'saving').display_user_balance()
user_kyle.display_user_balance()
# ------------------------------------------------Code---------------

# account_one = BankAccount(0.05, 100)
# account_two = BankAccount(0.02)

# account_one.display_account_info().deposit(25).deposit(25).deposit(25).withdraw(25).yield_interest().display_account_info()
# account_two.display_account_info().deposit(125).deposit(25).withdraw(10).withdraw(15).withdraw(15).withdraw(10).yield_interest().display_account_info()

# BankAccount.all_accounts_info()

