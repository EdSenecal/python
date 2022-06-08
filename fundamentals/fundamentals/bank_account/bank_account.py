class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.intrate = int_rate
        self.balance = 0 + balance
    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        return self
        #you would probably want to use an if statement here so that negative amounts can't be entered, but this should work

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self
        # your code here
    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
    def yield_interest(self):
        # your code here
        if self.balance >= 0:
            self.balance = self.balance * self.intrate
            return self
        else:
            print ("Sorry, today is un Interesting!  But for real you have no money")

# Jane_Doe = BankAccount(1.01, 500)
# john_doe = BankAccount(1.01, 1000)

# Jane_Doe.deposit(100).deposit(600).deposit(400).yield_interest().display_account_info()
# john_doe.deposit(100).withdraw(500).withdraw(400).withdraw(100).withdraw(100).yield_interest().display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user(self):
        print(self.account.balance)



