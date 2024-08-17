# Purpose: To demonstrate the banking operations using private, public, & protected methods
# Base class for bank admin
class BankAccount():
    # Initializes a bank account with an account number and balance
    def __init__(self, AC:str, balance:float)->None:
        self.__AC = AC                  #Private data
        self.__balance:float = balance  #Private data

    # Public getter function to access the private account information
    def get_AC(self) -> str:
        return self.__AC

    # Public getter function to access the private balance information
    def get_balance(self) -> float:
        return self.__balance

    # Deposits a specified amount into the account
    # If amount is positive, the amount is added to the account
    # If the amount is negative, an error message is displayed
    def deposit(self, amount:float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Total deposit: {amount} Total balance: {self.__balance}")
        else:
            print("Amount must be positive")

    # Withdraws a specified amount from the account
    # If the request is less than the balance, the amount is subtracted and processed
    # If the request is greater than the balance, an error message is displayed
    # If the request is negative, an error message is displayed
    def withdraw(self, amount:float) -> str:
        if amount > 0 and amount <= self.__balance:
            print(f"Withdrawing {amount} from balance")
            self.__balance -= amount
            print("New account balance is: ", self.__balance)
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            print("Please give a positive value to withdraw")

    # Displays account number and balance information
    def display_info(self) -> None:
        print("Account information", self.__AC)
        print("Balance information", self.__balance)

# Purpose: manage customer information and connected bank accounts
class Customer:
    # Initializes a new customer with name, email, and phone number, initializes with no accounts at first
    def __init__(self, name:str, email:str, phone:float) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []

    # Adds a bank account to the customer's list of accounts
    def add_account(self, account:BankAccount) -> None:
        self.accounts.append(account)

    # Displays details of the customer, with name, email, and phone, along with the bank account information
    def display_accounts_details(self) -> None:
        print(f"Customer name: {self.name}")
        print(f"Customer email: {self.email}")
        print(f"Customer phone: {self.phone}")

        # Displays each associated account's details
        for account in self.account:
            account.display_info()
