"""
HW 6.3
(Palindrome integer)
Write the functions with the following headers:

# Return the reversal of an integer, e.g. reverse(456) returns
# 654
def reverse(number):

# Return true if number is a palindrome
def isPalindrome(number)

Use the reverse function to implement isPalindrome. A number is a palindrome
if its reversal is the same as itself. Write a test program that prompts the
user to enter an integer and reports whether the integer is a palindrome.
"""


# Return the reversal of an integer, e.g. reverse(456) returns
# 654
def reverse(number):

    number_list = [char for char in str(number)]
    number_list.reverse()
    reverse_string = ''
    for x in number_list:
        reverse_string += x

    return int(reverse_string)


# Return true if number is a palindrome
def isPalindrome(number):

    # Negative numbers are not palindromic
    if number < 0:
        return False

    elif number == reverse(number):
        return True

    else:
        return False


while True:

    try:
        user_int = int(input('Please enter an integer: '))
        break

    except ValueError:
        print('Invalid format. You did not enter an integer.')
        continue

if isPalindrome(user_int) is True:
    print(user_int, 'is a palindrome.')

else:
    print(user_int, 'is NOT a palindrome.')
