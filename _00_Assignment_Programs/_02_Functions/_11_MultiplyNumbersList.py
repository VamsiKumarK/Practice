'''
Created on Nov 21, 2019

@author: Vamsi
'''

'''
Multiplying numbers in a list
'''

score = [2, 3, 4, 1, 8]
print("Given elements are: ", score)


def mult(data):
    total = 1
    for each in data:
        total *= each
    return total
    # Or we can write
    # for each in range(0, len(data)):
    # total *= data[each]
    # return total


result = mult(score)
print('Multiplication of the elements in the list is: ', result)
