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

#import pandas as pd

#weight_dict = {}

kilos = 1
max_value = 199

#kilo_list = []
#pound_list = []

print('Kilograms  Pounds')

while kilos < max_value + 1:
    pounds = format((kilos * 2.2), ".1f")
    #weight_dict[kilos] = pounds

    kilo_list.append(kilos)
    pound_list.append(pounds)

    kilo_str = format(str(kilos), "9s")
    pound_str = format(str(pounds), ">6s")
    weight_str = kilo_str + '  ' + pound_str
    print(weight_str)

    kilos += 1

"""
print('-------------------------------------------------------')

d = {'Kilograms': kilo_list, 'Pounds': pound_list}

df_1 = pd.DataFrame(data=d)
print(df_1)
"""
