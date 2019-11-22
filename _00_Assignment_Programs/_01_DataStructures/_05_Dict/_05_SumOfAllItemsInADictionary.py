'''
Created on Nov 19, 2019

@author: Vamsi
'''


'''
Adding all items in a Dictionary
'''
sum1 = 0
person = {'age': 24, 'height': 5.7, 'salary': 13000}
print('Elements in the Dictionary are: ', person.values())
for ele in person.values():
    sum1 = sum1 + ele
print('Sum of elements in the dictionary is: ', sum1)
