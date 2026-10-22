class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance: ₹", self.balance)


account1 = BankAccount("Tejas", 5000)

account1.display_balance()
