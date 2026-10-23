class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self._balance += amount
            print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print("Withdrawal successful")

    def display_balance(self):
        print("Balance: ₹", self._balance)


account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)
account.display_balance()

account.withdraw(10000)
account.deposit(-500)
