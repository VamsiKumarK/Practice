'''
Created on Nov 19, 2019

@author: Vamsi
'''

'''
Printing each item and values type in a Dictionary
'''

emp_data = {'eid': 100, 'name': 'Jack', 'age': 26, 'hikes': [23, 56, 76]}
for key, val in emp_data.items():
    print(key, ':', val)
for each in emp_data.values():  # Printing type of values
    print('Type of value is: ', type(each))
