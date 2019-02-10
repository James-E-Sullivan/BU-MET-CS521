"""
(Check SSN)
Write a program that prompts the user to enter a Social Security number in the
format ddd-dd-dddd, where d is a digit. The program displays 'Valid SSN' for a
correct Social Security number or 'Invalid SSN' otherwise.
"""

import sys

user_SSN = input("Please enter your Social Security Number in the format"
                 " XXX-XX-XXXX: ")

if len(user_SSN) != 11:
    print('Invalid SSN')
    sys.exit()

else:
    digit_slice = user_SSN[0:3] + user_SSN[4:6] + user_SSN[7:11]
    dash_slice = user_SSN[3] + user_SSN[6]

    for char in digit_slice:
        if char.isdigit():
            continue
        else:
            print('Invalid SSN')
            sys.exit()

    for char in dash_slice:
        if char != '-':
            print('Invalid SSN')
            sys.exit()

    print('Valid SSN')
