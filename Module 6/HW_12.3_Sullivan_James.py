"""
HW 12.3
(Game: ATM machine) **Automated Teller Machine machine???
Use the Account class created in Exercise 7.3 to simulate an ATM. Create ten
accounts in a list with the ids 0, 1, ..., 9, and an initial balance of $100.
The system prompts the user to enter an id. If the id is entered incorrectly,
ask the user to enter a correct id. Once an id is accepted, the main menu is
displayed as shown in the sample run. You can enter a choice of 1 for viewing
the current balance, 2 for withdrawing money, 3 for depositing money, and 4 for
exiting the main menu. Once you exit, the system will prompt for an id again.
So, once the system starts, it won't stop.
"""


class Account:

    def __init__(self, id_1=0, balance=100.00, annual_interest_rate=0.0):
        self.__id = id_1
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_monthly_interest(self):
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


def test_atm():

    account_list = [Account(x) for x in range(0, 10)]

    def enter_id():
        while True:
            try:
                user_id = int(input('Please enter an ID# from 0-9: '))

                if user_id in range(0, 10):
                    return user_id
                else:
                    continue

            except ValueError:
                print('Could not convert input to int. Try again.')
                continue

    def display_menu():
        print('\nMain menu')
        print('1: check balance')
        print('2: withdraw')
        print('3: deposit')
        print('4: exit')

    def enter_menu_option():
        while True:
            try:
                menu_option = int(input('Enter a choice: '))

                if menu_option in range(1, 5):
                    return menu_option
                else:
                    continue
            except ValueError:
                print('Could not convert input to int. Try again.')
                continue

    def menu_output(user_id, menu_option):
        if menu_option is 1:
            print('The balance is', round(account_list[user_id].get_balance(), 2))

        elif menu_option is 2:
            while True:
                try:
                    withdraw_amount = float(input('Enter an amount to withdraw: '))

                    if withdraw_amount >= 0:
                        break
                    else:
                        print('Invalid withdrawal amount.')
                        continue

                except ValueError:
                    print('Not a valid input. Try again.')
                    continue

            account_list[user_id].withdraw(withdraw_amount)

        elif menu_option is 3:
            while True:
                try:
                    deposit_amount = float(input('Enter an amount to deposit: '))

                    if deposit_amount >= 0:
                        break
                    else:
                        print('Invalid deposit amount.')
                        continue

                except ValueError:
                    print('Not a valid input. Try again.')
                    continue
            account_list[user_id].deposit(deposit_amount)

        elif menu_option is 4:
            print('')
            test_atm()

    account_id = enter_id()
    while True:

        display_menu()
        menu_choice = enter_menu_option()
        menu_output(account_id, menu_choice)


test_atm()
