class BankAccount:
    def __init__(self, name="Bill", balance=1000):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f'Account of {self.name} - Balance: {self.balance:.2f} euros'

account1 = BankAccount('Tim', 800)
account1.deposit(350)
account1.withdraw(200)
print(account1)
account2 = BankAccount()
account2.deposit(25)
print(account2)