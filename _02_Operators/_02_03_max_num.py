'''
Created on Nov 2, 2019

@author: User
'''
'''
Finding a maximum number
'''
num1 = int(input('enter a value '))
num2 = int(input('enter a value '))
num3 = int(input('enter a value '))
if num1 > num2 and num1 > num3:
    print('num1 is maximum number')
elif num2 > num1 and num2 > num3:
    print('num2 is maximum number')
else:
    print('num3 is maximum number')
