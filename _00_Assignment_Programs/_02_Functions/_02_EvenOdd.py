'''
Created on Nov 20, 2019

@author: Vamsi
'''

'''
printing even and odd numbers
'''


def evod(num):
    for each in range(1, num):
        if each % 2 == 0:
            print(each, end=',')

        elif each % 2 == 1:
            print(each)


evod(int(input('enter the range: ')))


'''
REFER AGAIN
'''
