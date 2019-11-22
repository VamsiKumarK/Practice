'''
Created on Nov 20, 2019

@author: Vamsi
'''


'''
converting list to tuple, set
'''

list1 = [23, 43, 56, 76, 43, True, 'Aleed', True]
print('Given list is: ', list1)
print('____________________________________________________')


def conv(data):
    s = set(data)
    print('After converting list in to set, Set is: ', s)
    print('____________________________________________________')
    t = tuple(data)
    print('After converting list in to tuple, Tuple is: ', t)


conv(list1)
