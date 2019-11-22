'''
Created on Nov 21, 2019

@author: Vamsi
'''

'''
Reversing a String
'''

player = 'StevenSmith'


def rev(data):
    data1 = data[::-1]
    return data1


res = rev(player)
print('Player string after Reverse is: ', res)
