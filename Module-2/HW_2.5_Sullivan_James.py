'''
(Financial application: calculate tips)
Write a program that reads the subtotal and the gratuity rate and computes
the gratuity and total. For example, if the user enters 10 for the
subtotal and 15% for the gratuity rate, the program displays 1.5 as the
gratuity and 11.5 as the total.
'''

subtotal, gratuityRate = eval(input('Enter the subtotal and gratuity rate'
                          'separated by commas: '))

gratuity = (subtotal * gratuityRate) / 100
total = subtotal - gratuity
print('The gratuity is', gratuity, 'and the total is', total)
