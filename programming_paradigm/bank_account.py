class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            return True
            self.account_balance -= amount
        else:
            return False
            print("Amount to be withdrawn is larger than the account balance. Cannot proceed.")
    
    def display_balance(self):
        print(f"Current Balance: $float({self.account_balance})")
    
