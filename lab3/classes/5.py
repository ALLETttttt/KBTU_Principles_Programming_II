class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'

    def deposit(self, quantity):
        self.balance += quantity
        return "Your Deposit Accepted"

    def withdraw(self, quantity):
        if quantity <= self.balance:
            self.balance -= quantity
            # print(self.balance)
            return "Withdraw is done"
        return "Withdraw unavailable"


a = Account('Bakdaulet', 1000000000)
print(a.deposit(500000))
print(a.withdraw(108000650))