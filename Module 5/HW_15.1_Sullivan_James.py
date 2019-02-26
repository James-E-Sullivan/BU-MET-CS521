"""
HW 15.1
(Sum the digits in an integer using recursion)
Write a recursive function that computes the sum of the digits in an integer.
Use the following function header:

def sumDigits(n):

For example, sumDigits(234) returns 2+3+4=9. Write a test program that prompts
the user to enter an integer and displays its sum.
"""


def sumDigits(n):
    """
    :param n: Any positive or negative integer
    :return: Returns the sum of each digit, using recursion
    """
    number_list = [digit for digit in str(n)]
    index = 0
    return int(number_list[index]) + sumDigitsHelper(n, index)


def sumDigitsHelper(n, index):
    """
    Helper function for sumDigits()
    :param n: Any positive or negative integer
    :param index: index used to determine which digit is being summed
    :return: Returns sum of the digit at index and each successive digit
    """

    index += 1
    number_list = [digit for digit in str(n)]

    if index == len(number_list) - 1:
        return int(number_list[index])

    else:
        return int(number_list[index]) + sumDigitsHelper(n, index)


while True:

    # Prompts user for integer, stores absolute value of input in user_int
    # Evaluates sum of digits. Does not take sign of entered number into consideration.
    try:
        user_int = abs(int(input('Enter an integer: ').strip()))
        break

    # User prompted again if the input is not a valid integer
    except ValueError:
        print('Not a valid input. Please try again.')
        continue

print(sumDigits(user_int))
