'''
Created on Nov 13, 2019

@author: Vamsi
'''

'''
Removing even elements in a list using for loop
'''

score = [12, 77, 44, 54, 92, 76, 88]
score1 = []
print('Given numbers in the list: ', score)
for each in score:
        score1.append(each)
        for each in score1:
            if each % 2 == 0:       # finding even numbers in the loop
                score1.remove(each)
print('Numbers with out even numbers: ', score1)
print('_________________________________________')

'''
Removing even elements in a list using range
 '''

'''score = [12, 54, 79, 43, 55, 98, 77, 88]
print('Given numbers in the list: ', score)
for each in range(len(score)):
    if score[each] % 2 == 0:
        score.pop(each)
print('Numbers with out even numbers: ', score)
'''
