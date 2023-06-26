from app.calculations import add, subtract, multiply, divide, BankAccount
import pytest


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (5, 3, 8),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected


def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(20, 5) == 4

@pytest.fixture
def zero_bank_account():

    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(starting_balance=50)


def test_bank_set_initial_amount(bank_account):

    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0 

def test_withdraw(bank_account):
    bank_account.withdraw(20)

    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)

    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()

    assert int(bank_account.balance) == 55


@pytest.mark.parametrize("deposited, withdrawed, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000),
])
def test_bank_transaction(zero_bank_account, deposited, withdrawed, expected ):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrawed)

    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(Exception):
        bank_account.withdraw(200)

