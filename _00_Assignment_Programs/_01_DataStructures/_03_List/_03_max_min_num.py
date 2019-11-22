'''
Created on Nov 12, 2019

@author: Vamsi
'''
'''
finding minimum number in a list
'''

score = [94, 34, 94, 67, 3, 768, 34]
min_num = score[0]
for each in score:
    if each < min_num:
        min_num = each
print('min_num in the given list is: ', min_num)
print('end')

'''
finding maximum number in a list
'''
score = [34, 94, 67, 3, 768, 34]
max_num = score[0]
for each in score:
    if each > max_num:
        max_num = each
print('max_num in the given list is: ', max_num)
