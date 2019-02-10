"""
(Algebra: solve 2x2 linear equations)
You can use Cramer's rule to solve the following 2x2 system of linear equation:

ax + by = e
cx + dy = f

x = (ed - bf) / (ad - bc)
y = (af - ec) / (ad - bc)

Write a program that prompts the user to enter
a, b, c, d, e, and f
and display the result.

If (ad - bc) is 0, report that "The Equation has no solution."
"""

# simultaneous assignment of values from user input
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

# if (ad - bc) is 0, 'The Equation has no solution' is printed
if (a * d) - (b * c) == 0:
    print("The Equation has no solution")

# Otherwise, calculations are completed and x and y values printed
else:

    x = ((e * d) - (b * f)) / ((a * d) - (b * c))
    y = ((a * f) - (e * c)) / ((a * d) - (b * c))

    print("x is", x, "and y is", y)
