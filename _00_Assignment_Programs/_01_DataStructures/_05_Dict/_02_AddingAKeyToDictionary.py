'''
Created on Nov 19, 2019

@author: Vamsi
'''


'''
Adding a new key to the dictinary
'''
'''
data1 = {'eid': 100, 'name': 'Jack', 'age': 26, 'hikes': [23, 56, 76]}
data2 = {'company': 'oracle'}
data1.update(data2)     # updating key using update method



print(data1)
'''

data2 = {}

print('adding new key in to dict:', data2.setdefault('Location', 'hars'))
'''updates in the dict with location key
'''
print('dict after adding new key is: ', data2)

'''
get() function function will returns the default none value to the key,
it doesn't update in the dict
'''
