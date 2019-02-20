"""
HW 14.1
(Display keywords)
Revise Listing 14.4 CountKeywords.py to display the key-words in a Python source
file as well as to count the number of keywords.

Known issues: This script will read any instance of keyWords, even in comments.
"""

import os.path
import sys


def main():

    keyWords = {'and', 'as', 'break', 'class',
                'continue', 'def', 'del', 'elif', 'else'
                'except', 'False', 'finally', 'for', 'from'
                'global', 'if', 'import', 'in', 'is', 'lambda',
                'None', 'nonlocal', 'not', 'or', 'pass', 'raise',
                'return', 'True', 'try', 'while', 'with', 'yield'}

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename):  # Check if file exists
        print('File', filename, 'does not exist')
        sys.exit()

    infile = open(filename, 'r')  # Read and split words from the file

    text = infile.read().split()  # Read and split words from the file

    keyWord_dict = {}

    # Create dictionary w/ keyWords as keys, and count as value
    for word in keyWords:
        keyWord_dict[word] = 0

    # Increment count value if key word is in text
    for word in text:
        if word in keyWords:
            keyWord_dict[word] += 1

    # Print keyWords that were found in text, along with counts
    for key in keyWord_dict:
        if keyWord_dict[key] is 0:
            continue

        elif keyWord_dict[key] is 1:
            print(key, 'occurs', keyWord_dict[key], 'time')

        else:
            print(key, 'occurs', keyWord_dict[key], 'times')

main()
