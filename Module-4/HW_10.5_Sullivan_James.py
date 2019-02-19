"""
10.5 (Print distinct numbers)
Write a program that reads in numbers separated by a space in one line and
displays distinct numbers (i.e., if a number appears multiple times, it is
displayed only once). (Hint: Read all the numbers and store them in list1.
Create a new list list2. Add a number in list1 to list2. If the number is
already in the list, ignore it.) Here is a sample run of the program:

Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
The distinct numbers are: 1 2 3 6 4 5
"""


def get_ten_numbers():

    while True:
        try:
            user_int_list = [int(input_int) for input_int in input(
                'Enter ten numbers (separated by spaces): ').split()]
            if len(user_int_list) is not 10:
                print('You did not enter ten numbers.')
                user_int_list = get_ten_numbers()
            break

        except ValueError:
            print('Not a valid input.')

    return user_int_list


def get_distinct_numbers(ten_number_list):

    ten_number_set = set(ten_number_list)
    distinct_list = list(ten_number_set)
    return distinct_list


ten_numbers = get_ten_numbers()
distinct_numbers = get_distinct_numbers(ten_numbers)

distinct_numbers_string = ''
for number in distinct_numbers:
    distinct_numbers_string += str(number) + ' '


print('The distinct numbers are:', distinct_numbers_string)
