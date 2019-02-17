'''
Homework 10.3
(Count occurrence of numbers)
Write a program that reads some integers between 1 and 100 and counts the
occurrences of each.
'''



count_list = []
for number in range(1, 101):
    count_list.append(number)

number_dict = {}
for number in number_dict:
    '''
    '''


def prompt_input():

    input_int_list = [int(input_int) for input_int in input(
        'Enter integers (1-100), separated by spaces: ').split()]

    return input_int_list


#x = True
while True:

    try:

        user_int_list = prompt_input()

        for element in user_int_list:

            if element not in count_list:
                print('One or more numbers entered are outside the required'
                      ' range. Please enter number between 1 and 100.')
                user_int_list = prompt_input()

        break

    except ValueError:

        print('Not a valid input. Please enter an integer between 1-100.')
        user_int_list = prompt_input()




print(user_int_list)
print(count_list)


'''
for number in input_int_list:
    
'''