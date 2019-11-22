'''
Created on Nov 4, 2019

@author: Vamsi
'''

'''
dynamically printing even numbers
'''

mn, mx = [int(input('enter the minimum and maximum range:')).split(',')]
x = mn
if x % 2 != 0:
    x += 1
while x >= mn and x <= mx:
    print(x)
    x += 2
print('end')
