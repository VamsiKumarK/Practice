'''
Created on Nov 12, 2019

@author: Vamsi
'''

''' removing duplicate elements is a list using set'''

marks = [23, 234, 43, 345, 43, 234, 43]
print('Original List is : ', marks)
marks = list(set(marks))
print('List after removing duplicates', marks)
print('______________________________')

'''
 removing duplicate elements using dictionaries
'''
data = ['Python', 'Java', 'Kala', 'Python', 'Kala', 23, 55, True, 23, 67, True]
print('Original List is : ', data)
data = list(dict.fromkeys(data))
print(data)
print('List after removing duplicates', data)
print('______________________________')
print('______________________________')


'''
Removing duplicates using for loop and Range function
'''
new_format = []
_format = [23, 234, 43, 67, 43, 290, 43]
for ele in range(len(_format)):
    if _format[ele] not in new_format:
        new_format.append(_format[ele])
print(new_format)
print('______________________________')


'''
Removing duplicates using for loop function
'''
marks1 = []
marks = [23, 234, 43, 345, 43, 234, 43]
for each in marks:
    if each not in marks1:
        marks1.append(each)
print(marks1)
