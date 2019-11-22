'''
Created on Nov 21, 2019

@author: Vamsi
'''


'''
Finding maximum of three numbers
'''


age1 = int(input('Enter the First number: '))
age2 = int(input('Enter the Second number: '))
age3 = int(input('Enter the Third number: '))


def large(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# print('the maximum number is: ', large(age1, age2, age3))
max_num = large(age1, age2, age3)
print('The maximum number from the given three is: ', max_num)
