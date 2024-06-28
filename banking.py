class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute for data hiding and protection
    
    # Public method to get the balance
    def get_balance(self):
        return self.__balance  # Controlled access
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")
    
# Usage
account = Account("Alice", 1000)
print(account.owner)  # Public attribute
print(account.get_balance())  # Accessing private attribute via getter

account.deposit(500)  # Depositing money
account.withdraw(200)  # Withdrawing money