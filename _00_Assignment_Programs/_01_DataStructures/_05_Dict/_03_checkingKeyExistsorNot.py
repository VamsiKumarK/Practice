'''
Created on Nov 19, 2019

@author: Vamsi
'''


'''
checking if a key already exists in the dictionary or not
'''


emp_data = {'eid': 100, 'name': 'Jack', 'age': 26, 'hikes': [23, 56, 76]}
print(emp_data)
for each in emp_data:
    if each == 'eid':
        print('{} key exists in the dict'.format(each))

print('end')
