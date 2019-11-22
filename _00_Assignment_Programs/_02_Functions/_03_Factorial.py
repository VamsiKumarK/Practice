'''
Created on Nov 20, 2019

@author: Vamsi
'''


'''
finding factorial of a given number using while loop
'''

num = 5


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


print('The factorial of given number: ', factorial(num))
print("__________________________________________________")

'''
using recursive
'''


def fact(num1):
    if num1 == 0 or num1 == 1:
        return 1
    else:
        num1 = num1 * factorial(num1 - 1)
    return num1


print('The factorial of given number: ', fact(5))
