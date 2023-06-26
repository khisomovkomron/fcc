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


def test_bank_set_initial_amount():
    bank_account = BankAccount(starting_balance=50)

    assert bank_account.balance == 50

def test_bank_default_amount():
    bank_amount = BankAccount()
    assert bank_amount.balance == 0 