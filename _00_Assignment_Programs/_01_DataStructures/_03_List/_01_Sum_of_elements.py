'''
Created on Nov 12, 2019

@author: Vamsi
'''
'''adding elements in a list'''


total = 0
marks = [30, 40, 55, 100, 46, 90]
print('marks :', marks)
for each in range(0, len(marks)):   # Iterating through the range of list
    total = total + marks[each]
print('sum of subjects in marks is', total)

'''print(sum(marks))       # Adding elements in list using sum() function.'''


'''
Adding elements in a list using for loop
'''
total = 0
marks = [30, 40, 55, 100, 46, 90]
print('marks :', marks)
for each in marks:   # Iterating through the range of list
    total += each
print('sum of subjects in marks is', total)
