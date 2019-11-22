'''
Created on Nov 2, 2019

@author: User
'''

'''
marks of students using simple if else condition
'''
marks = int(input("enter the value "))
if marks >= 65:
    print('first class')
elif marks >= 50 and marks < 65:
    print('second class')
elif marks >= 35 and marks < 50:
    print('third class')
else:
    print('fail')
