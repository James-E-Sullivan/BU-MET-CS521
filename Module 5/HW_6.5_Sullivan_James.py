"""
HW 6.5
(Sort three numbers)
Write the following function to display three numbers in increasing order:

def displaySortedNumbers(num1, num2, num3):

Write a test program that prompts the user to enter three numbers and invokes
the function to display them in increasing order. Here are some sample runs:

Enter three numbers: 3, 2.4, 5
The sorted numbers are 2.4 3 5
"""


def displaySortedNumbers(num1, num2, num3):
    """
    Takes in 3 input numbers in any order, sorts them, then prints
    the sorted numbers on one line
    """
    numbers = [num1, num2, num3]
    numbers.sort()
    print('The sorted numbers are', end=' ')
    for i in numbers:
        print(i, end=' ')


while True:

    try:
        # List comprehension appends input numbers into list
        user_numbers = [x for x in input(
            'Enter three numbers: ').strip().split()]

        # If the length of the list is not 3, user prompted again
        if len(user_numbers) is not 3:
            continue

        # If length of list is 3, program continues
        else:
            break

    # If user does not input a number, user prompted again
    except ValueError:
        continue

# The three user numbers are input into displaySortedNumbers function
displaySortedNumbers(user_numbers[0], user_numbers[1], user_numbers[2])

