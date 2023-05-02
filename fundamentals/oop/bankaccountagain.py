

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
    
    def __repr__(self):
        return (f"Balance: {self.balance}")

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Balance is: {account.balance} Interest rate: {account.int_rate}")

# --------------------------------------------User class------------

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        self.accounts['checking'] = BankAccount(0.02, 200)

    def create_account(self, account_name):
        for names in self.accounts:
            print(names)
            if account_name == names:
                print("Account already created")
                return self
        self.accounts[account_name] = BankAccount(0.02)
        return self

    def make_deposit(self, amount, account):
        self.accounts[account].deposit(amount)
        return self

    def make_withdrawal(self, amount, account):
        self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self):

        print(f"{self.name} {self.accounts}")
        return self

    def transfer_money(self, amount, account, other_user, other_user_account):
        self.accounts[account].withdraw(amount)
        other_user.accounts[other_user_account].deposit(amount)
        return self





user_guy = User('Guy', 'faker@email.com')
user_kyle = User('Kyle', 'fake@email.com')
user_kyle.make_deposit(25, 'checking').make_withdrawal(50, 'checking').display_user_balance().create_account('saving')
user_kyle.make_deposit(100, 'saving').display_user_balance().transfer_money(50, 'checking', user_guy, 'checking')
user_guy.display_user_balance().create_account('checking').display_user_balance()

# ------------------------------------------------Code---------------

# account_one = BankAccount(0.05, 100)
# account_two = BankAccount(0.02)

# account_one.display_account_info().deposit(25).deposit(25).deposit(25).withdraw(25).yield_interest().display_account_info()
# account_two.display_account_info().deposit(125).deposit(25).withdraw(10).withdraw(15).withdraw(15).withdraw(10).yield_interest().display_account_info()

# BankAccount.all_accounts_info()

