'''
Created on Nov 19, 2019

@author: Vamsi
'''

'''
Multiplying all items in the Dictionary
'''

tot = 1
data1 = {'age': 24, 'height': 10, 'salary': 20000}
print('Elements in the Dictionary are: ', data1.values())
for each in data1.values():
    tot *= each
print('Multiplication of all elements in dict is: ', tot)
