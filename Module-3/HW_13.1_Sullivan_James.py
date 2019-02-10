"""
(Remove text)
Write a program that removes all the occurrences of a specified string from a
text file. Your program should prompt the user to enter a filename and a
string to be removed. Here is a sample run:

Enter a filename: test.txt
Enter the string to be removed: morning
Done
"""


# Loop used for exception handling
while True:
    filename = input('Enter a filename: ').strip()

    try:
        infile = open(filename, 'r')
        file_string = infile.read()
        infile.close()
        break

    except IOError:
        print("File " + filename + ' does not exist. Try again.')


# Prompts user for a substring to be removed from the text file
replacement_text = input('Please enter text to be removed from the file: ')

# Replaces any instance of the user substring with an empty string
new_file_string = file_string.replace(replacement_text, '')

# Output file opened, new_file_string written to file, file closed
outfile = open('13.1_output.txt', 'w')
outfile.write(new_file_string)
outfile.close()

print('Done')
