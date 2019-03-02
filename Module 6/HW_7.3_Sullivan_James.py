"""
HW 7.3
(The Account class)
Design a class named Account that contains:

* A private int data field named 'id' for the account
* A private float data field named 'balance' for the account
* A private float data field named annualInterestRate that stores the current
    interest rate.
* A constructor that creates an account with the specified id (default 0),
    initial balance (default 100), and annual interest rate (default 0)
* The accessor and mutator methods for id, balance, and annualInterestRate
* A method named getMonthlyInterestRate() that returns the monthly interest
    rate
* A method named withdraw that withdraws a specified amount from the account
* A method named deposit that deposits a specified amount to the account

Draw a UML diagram for the class, and then implement the class. (Hint: The
method getMonthlyInterest() is to return the monthly interest amount, not the
interest rate. Use this formula to calculate the monthly interest:

    balance * monthlyInterestRate
    where monthlyInterestRate == annualInterestRate / 12

Note that annualInterestRate is a percent (like 4.5%). You need to divide it
by 100.

Write a test program that creates an Account object with an account id of 1122,
a balance of $20,000, and an annual interest rate of 4.5%. Use the withdraw
method to withdraw $2,500, use the deposit method to deposit $3,000, and print
the id, balance, monthly interest rate, and monthly interest.
"""


class Account:

    def __init__(self, id_1=0, balance=100.00, annual_interest_rate=0.0):
        self.__id = id_1
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def getMonthlyInterest(self):
        monthly_interest_rate = self.__annual_interest_rate / 12
        return (self.__balance * monthly_interest_rate) / 100

    def get_monthly_interest_rate(self):
        return self.__annual_interest_rate / 12

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def set_annual_interest_rate(self, new_annual_interest_rate):
        self.__annual_interest_rate = new_annual_interest_rate

    def withdraw(self, withdraw_amount):
        self.set_balance(self.__balance - withdraw_amount)

    def deposit(self, deposit_amount):
        self.set_balance(self.__balance + deposit_amount)


def testAccount():
    """
    Tests account class methods.
    Creates account_1 with id: 1122, initial balance: $20,000, annual interest rate: 4.5%.
    Withdraws $2500 with self.withdraw() method
    Deposits $3000 with self.deposit() method
    Prints ID (1122), Balance ($20,500.00), Monthly Interest Rate (0.375%), and Monthly interest ($76.88)
    Monthly interest is calculated after self.withdraw() and self.deposit() methods used.
    """
    account_1 = Account(1122, 20000.00, 4.5)

    account_1.withdraw(2500)
    account_1.deposit(3000)

    print('ID:', account_1.get_id())
    print('Balance:', format(account_1.get_balance(), "0.2f"))
    print('Monthly interest rate:', account_1.get_monthly_interest_rate())
    print('Monthly interest:', round(account_1.getMonthlyInterest(), 2))


testAccount()
