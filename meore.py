class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")


account = BankAccount("გიორგი", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  
account.get_balance()


savings = SavingsAccount("მარია", 2000, 0.05)  
savings.deposit(1000)
savings.apply_interest()
savings.get_balance()
