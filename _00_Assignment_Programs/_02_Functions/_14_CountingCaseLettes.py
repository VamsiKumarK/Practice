'''
Created on Nov 21, 2019

@author: Vamsi
'''

'''
Counting UpperCase and LowerCase Letters in a String
'''

text1 = input('Enter any String: ')


def case(data1):
    count1 = 0
    count2 = 0
    for each in data1:
        if (each.isupper()):
            count1 += 1
        elif (each.islower()):
            count2 += 1
    print('no of UpperCase Letters in the string is: ', count1)
    print('no of LowerCase Letters in the string is: ', count2)


case(text1)
