#From the actual file, import everything (*)
from BankAccount import *

# Tests for BankAccount class
def test_account():
    # Create bank account objects
    account1 = BankAccount("23478", 10873.42)
    account2 = BankAccount("Chris", 27495.95)

    assert account1.get_AC() == "23478"
    assert account1.get_balance() == 10873.42

    assert account2.get_AC() == "Chris"
    assert account2.get_balance() == 27495.95

def test_deposit():
    account = BankAccount("23478", 10873.42)
    account.deposit(550.00)

    assert account.get_balance() == 11423.42

def test_withdraw():
    account = BankAccount("23478", 11423.42)
    account.withdraw(550.00)

    assert account.get_balance() == 10873.42

def test_insufficient_fund():
    account = BankAccount("7845", 3400.0)
    account.withdraw(3500.0)

    assert account.get_balance() == 3400

def test_deposit_negative_amount():
    account = BankAccount("12345", 1000.0)
    account.deposit(-500.0)

    assert account.get_balance() == 1000.0

def test_withdraw_negative_amount():
    account = BankAccount("12345", 1000.0)
    account.withdraw(-500.0)

    assert account.get_balance() == 1000.0

def test_withdraw_exceeding_balance():
    account = BankAccount("67890", 500.0)
    account.withdraw(600.0)

    assert account.get_balance() == 500.0


def test_multiple_deposits_and_withdrawals():
    account = BankAccount("67890", 1000.0)
    account.deposit(200.00)
    account.withdraw(150.00)
    account.deposit(50.00)

    assert account.get_balance() == 1100.00



# Tests for Customer Class
def test_customer_initialization():
    customer = Customer("Joe Rudster", "jrudster@yahoo.com", 5416729173)

    assert customer.name == "Joe Rudster"
    assert customer.email == "jrudster@yahoo.com"
    assert customer.phone == 5416729173
    assert len(customer.accounts) == 0

def test_add_account():
    customer = Customer("Alexa Smith", "alexasmith@gmail.com", 7023649203)
    account = BankAccount("12345", 1000.00)
    customer.add_account(account)

    assert len(customer.accounts) == 1
    assert customer.accounts[0] == account

def test_multiple_accounts():
    customer = Customer("Nathan Parker", "parknate@aol.com", 8137846712)
    account1 = BankAccount("35898", 2000.00)
    account2 = BankAccount("64832", 3000.00)
    customer.add_account(account1)
    customer.add_account(account2)

    assert len(customer.accounts) == 2
    assert customer.accounts[0] == account1 and customer.accounts[1] == account2
