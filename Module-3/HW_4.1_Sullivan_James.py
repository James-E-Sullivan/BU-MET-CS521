"""
(Algebra: solve quadratic eqautions)
The two roots of a quadratic equation, for example, ax^2 + bx + c = 0,
can be obtained using the following formula:

r1 = (-b + sqrt((b^2)-4ac)) / 2a
r2 = (-b - sqrt((b^2)-4ac)) / 2a

b^2 - 4ac is called the discriminant of the quadratic equation.
If it is positive, the equation has two real roots.
If it is zero, the equation has one root. If it is negative,
the equation has no real roots.

Write a program that prompts the user to enter values for a, b, and c
and displays the result based on the discriminant. If the discriminant
is positive, display two roots. If the discriminant is 0, display one root.
Otherwise, display "The equation has no real roots."
"""

a, b, c = eval(input("Enter a, b, c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:

    r_1 = (-b + discriminant) / (2 * a)
    r_2 = (-b - discriminant) / (2 * a)

    print("The roots are", r_1, "and", r_2)

elif discriminant == 0:

    r_1 = (-b + discriminant) / (2 * a)

    print("The root is ", r_1)

else:

    print("The equation has no real roots.")
