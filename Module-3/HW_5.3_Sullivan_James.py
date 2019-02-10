"""
(Conversion from kilograms to pounds)
Write a program that displays the following table
(note that 1 kilogram is 2.2 pounds):

Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.6
"""

# Assigns maximum kilogram value for table
max_value = 199

# Prints header for table
print('Kilograms  Pounds')

# Loops from 1 to 199, using 'kilos' as the index
# Calculates 'pounds' based on value of kilos, and prints formatted values
for kilos in range(1, max_value + 1):

    pounds = kilos * 2.2

    print(format(kilos, "<9d") + '  ' + format(pounds, ">6.1f"))

    kilos += 1
