'''
Created on Nov 6, 2019

@author: Vamsi
'''

'''
Basic continue statement While loop
'''

count = 10
while count < 100:
    count += 10
    if count == 80:
        continue

    print(count)

print('the end')
