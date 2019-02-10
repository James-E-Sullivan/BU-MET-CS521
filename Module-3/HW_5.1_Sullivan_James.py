"""
(Count positive and negative numbers and compute the average of numbers)
Write a program that reads an unspecified number of integers, determines
how many positive and negative values have been read, and computes the
total and average of the input values (not counting zeroes). Your
program ends with the input '0'. Display the average as a floating-point
number.
"""

positives = 0
negatives = 0
count = 0
total = 0

while True:

    # User prompted for integer
    user_int = eval(input("Enter an integer, the input ends if it is 0: "))

    # If user enters 0 before entering an integer, user prompted again
    if user_int == 0 and count == 0:
        print("You didn't enter any number")
        continue

    # If user enters 0 after entering at least 1 int, loop exits
    elif user_int == 0 and count > 0:
        break

    # If user enters int, count incremented, int added to total, and
    # positives or negatives incremented, depending on value.
    else:
        count += 1
        total += user_int

        if user_int > 0:
            positives += 1

        elif user_int < 0:
            negatives += 1

# Prints positives, negatives, total, and average values
print("The number of positives is", positives)
print("The number of negatives is", negatives)
print("The total is", total)
print("The average is", total / count)
