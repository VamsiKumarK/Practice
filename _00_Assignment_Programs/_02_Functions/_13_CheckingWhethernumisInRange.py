'''
Created on Nov 21, 2019

@author: Vamsi
'''

'''
Checking Number is in range or not
'''

num1 = int(input('Enter the number: '))
num2 = int(input('Enter starting range: '))
num3 = int(input('Enter ending range: '))


def check(n1, n2, n3):
    if n1 in range(n2, n3):
        print('Entered number is in range')
    else:
        print('Entered number is not in range')


check(num1, num2, num3)
