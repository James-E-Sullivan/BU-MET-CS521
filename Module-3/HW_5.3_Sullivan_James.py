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

import pandas as pd

max_value = 199

kilo_list = []
pound_list = []

print('Kilograms  Pounds')

for kilos in range(1, max_value + 1):

    pounds = kilos * 2.2

    kilo_list.append(kilos)
    pound_list.append(pounds)

    print(format(kilos, "<9d") + '  ' + format(pounds, ">6.1f"))

    kilos += 1

"""
print('-------------------------------------------------------')

d = {'Kilograms': kilo_list, 'Pounds': pound_list}

df_1 = pd.DataFrame(data=d)
print(df_1.to_string(index=False))
"""
