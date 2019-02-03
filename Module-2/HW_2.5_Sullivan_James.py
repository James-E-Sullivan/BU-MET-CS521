'''
(Financial application: calculate tips)
Write a program that reads the subtotal and the gratuity rate and computes
the gratuity and total. For example, if the user enters 10 for the
subtotal and 15% for the gratuity rate, the program displays 1.5 as the
gratuity and 11.5 as the total.
'''

# Prompts user for subtotal and gratuity rate, assigns them to variables
subtotal, gratuityRate = eval(input('Enter the subtotal and gratuity rate'
                          ' separated by commas: '))

# Calculates the gratuity owed, based on the subtotal and gratuity rate
gratuity = round(((subtotal * gratuityRate) / 100), 2)  # Round to 2 decimals

# Calculates total amount owed by adding subtotal to gratuity
total = round((subtotal + gratuity), 2)  # Round to 2 decimals

# Gratuity and total displayed on console
print('The gratuity is', gratuity, 'and the total is', total)
