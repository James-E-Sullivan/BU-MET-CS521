"""
Homework 10.3
(Count occurrence of numbers)
Write a program that reads some integers between 1 and 100 and counts the
occurrences of each.
"""


def prompt_input():
    """
    Prompts user for integers, separated by spaces. Input string is split into
    a list (user_int_list) and returned. Checks for invalid inputs and prompts
    user again if necessary.
    :return user_int_list:
    """
    while True:
        try:
            user_int_list = [int(input_int) for input_int in input(
                'Enter integers (1-100), separated by spaces: ').split()]

            for element in user_int_list:

                if element not in range(1, 101):
                    print('One or more numbers entered are outside the required'
                          ' range. Please enter numbers between 1 and 100.')
                    user_int_list = prompt_input()

            break

        except ValueError:
            print('Not a valid input. Please enter an integer between 1-100.')

    return user_int_list


def count_numbers(integer_list):
    """
    :param integer_list: List of integers
    :return count_list: List with the count of each integer between 1-100 in
    integer list.
    """

    count_list = 100 * [0]

    for number in integer_list:

        count_list[number - 1] += 1

    return count_list


def display_count(count_list):
    """
    :param count_list: List with the count of integers (corresponding to
    index - 1).
    Prints out the integer and count for each integer with a count > 0.
    """
    for number in range(len(count_list)):

        if count_list[number] is 0:
            continue

        elif count_list[number] is 1:
            current_integer = number + 1
            count = count_list[number]
            print(current_integer, 'occurs', count, 'time')

        else:
            current_integer = number + 1
            count = count_list[number]
            print(current_integer, 'occurs', count, 'times')


final_count_list = count_numbers(prompt_input())
display_count(final_count_list)
