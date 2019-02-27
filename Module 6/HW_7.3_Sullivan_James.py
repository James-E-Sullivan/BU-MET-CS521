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
