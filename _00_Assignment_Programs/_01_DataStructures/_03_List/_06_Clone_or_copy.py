'''
Created on Nov 13, 2019

@author: Vamsi
'''


'''
Copying or cloning a list using copy and append function
'''
old_list = [223, 23, 90, 563, 45]
print('elements in old list is: ', old_list)
new_list = []
print('elements in new list is: ', new_list)
new_list = old_list.copy()        # copies list1 elements in to list2

''' list2.append(list1) appends each element in to new list'''

print('Elements in new list after cloning is: ', new_list)
id
print('_________________________________')
'''
using for loop
'''
old_list = [223, 23, 90, 454, 22]
print('Elements in old list is: ', old_list)
new_list = []
print('Elements in new list is: ', new_list)
for ele in old_list:
    new_list.append(ele)
print('Elements in new list after cloning is: ', new_list)
print('reference of old list is:', id(old_list))
print('reference of new list is:', id(new_list))


'''
We can assign old list to new list using assignment operators
like new list = old list
'''
