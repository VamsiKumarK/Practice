'''
Created on Nov 21, 2019

@author: Vamsi
'''


'''
Printing Multiplication Table of a number
'''

num1 = int(input('Enter the Number: '))
print('Multiplication Table of Entered number is: ')


def mult(num2):
    for each in range(1, 11):
        print(num2, 'x', each, '=', num2*each)


mult(num1)
