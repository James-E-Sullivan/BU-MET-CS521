"""
HW 15.3
(Compute greatest common divisor using recursion)
The gcd(m, n) can also be defined recursively as follows:

* If m % n is 0, gcd(m, n) is n
* Otherwise, gcd(m, n) is gcd(n, m % n)

Write a recursive function to find the GCD. Write a test program that prompts
the user to enter two integers and displays their GCD.
"""


def gcd(m, n):
    """
    :param m: Any integer
    :param n: Any integer
    :return: Returns greatest common denominator of m and n
    """

    # To avoid modulo by 0. GCD of (0, x) will be x
    if n is 0:
        return abs(m)

    elif m % n is 0:
        return abs(n)

    else:
        return gcd(n, (m % n))


while True:

    # Prompts user to two integers
    try:
        user_ints = [int(value) for value in input(
            'Enter two integers, separated by a space: ').split()]

        # User prompted again if number of inputs is not 2.
        if len(user_ints) is not 2:
            print('Incorrect number of integers. Please try again.')
            continue

        break

    # If any input is not an int, user prompted again.
    except ValueError:
        print('Input is not an integer. Please try again.')
        continue

# Displays GCD of user inputs
print(gcd(user_ints[0], user_ints[1]))
