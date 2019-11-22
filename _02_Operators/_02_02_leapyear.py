'''
Created on Nov 2, 2019

@author: User
'''
'''
leap year with if else
'''
year = int(input('enter a value '))
if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print('{} is a leap year'.format(year))
        else:
            print('{} is not a leap year'.format(year))
    else:
        print('{} is a leap year'.format(year))
else:
    print('{},is not a Leap year'.format(year))
