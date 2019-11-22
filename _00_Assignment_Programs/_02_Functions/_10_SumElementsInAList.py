'''
Created on Nov 21, 2019

@author: Vamsi
'''
'''
Adding elements in a list
'''

data = [24, 23, 34, 67, 89]
print("Given elements are: ", data)


def add(sum1):
    total = 0
    for each in sum1:
        total += each
    return total
    # Or we can write
    # for each in range(0, len(sum1):
    # tot += sum1[each]


score = add(data)
print('Sum of the elements in the list is: ', score)
