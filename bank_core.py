"""
This is banking system core module.
It contains the Account class and its subclasses.
The Account class is the parent class for the SavingsAccount and CheckingAccount classes.
The Account class has the following methods:
- login(username, password): Logs a user into their account.
- deposit(amount): Deposits money into the account.
- withdraw(amount): Withdraws money from the account.
- get_balance(): Returns the account balance.
- logout(): Logs a user out of their account.
"""

class Account: #Parent class
    def __init__(self, username, password, balance=0.0): #Constructor
        self._username = username #Encapsulation
        self._password = password 
        self._balance = balance
    
    def login(self, username, password):
        if self._username == username and self._password == password: #Ensure the username and password match
            print(f"Login successful! Welcome, {self._username}.")
            return True
        else:
            raise ValueError("Invalid login credentials!")
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be greater than 0.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def get_balance(self):
        return self._balance
    
    def logout(self):
        print(f"{self._username} has logged out.")

class SavingsAccount(Account): # Class for savings account
    def __init__(self, username, password, balance=0.0, interest_rate=0.03):
        super().__init__(username, password, balance)
        self._interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self._balance * self._interest_rate
        print(f"Interest earned: ${interest}")
        return interest
    
    def account_type(self):
        return "Savings Account"

class CheckingAccount(Account): #Class for checking account
    def __init__(self, username, password, balance=0.0, overdraft_limit=100):
        super().__init__(username, password, balance)
        self._overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and (self._balance + self._overdraft_limit) >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self._balance}")
        else:
            print("Insufficient funds (Overdraft limit exceeded).")
    
    def account_type(self):
        return "Checking Account"

# --- Account Creation ---
print("Welcome to Start_Hub Innovation Bank!")
print("Create an account to get started.")
print("=======================================")
username = input("Enter a username: ")
password = input("Enter a password: ")

account_choice = input("Choose account type (Savings/Checking): ").strip().lower()

if account_choice == "savings":
    account = SavingsAccount(username, password)
elif account_choice == "checking":
    account = CheckingAccount(username, password)
else:
    print("Invalid account type. Exiting program.")
    exit()

# --- User Login ---
print("\nPlease log in:")
login_user = input("Username: ")
login_pass = input("Password: ")

try:
    if account.login(login_user, login_pass):
        print(f"You are logged into a {account.account_type()}")
        
        # --- Perform Transactions ---
        while True:
            print("\nChoose an option: \n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Calculate Interest (Savings Only)\n5. Logout")
            option = input("Enter your choice: ")

            if option == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif option == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif option == "3":
                print(f"Your balance is: ${account.get_balance()}")
            elif option == "4" and isinstance(account, SavingsAccount):
                account.calculate_interest()
            elif option == "5":
                account.logout()
                break
            else:
                print("Invalid option. Try again.")

except ValueError as e:
    print(e)
