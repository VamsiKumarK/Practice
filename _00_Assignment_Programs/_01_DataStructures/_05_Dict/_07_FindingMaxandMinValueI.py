'''
Created on Nov 19, 2019

@author: Vamsi
'''


'''
Finding max num in dictionaries using for loop
'''

data3 = {'a': 10, 'b': 34, 'c': 78, 'e': 8}
print('Given Dictionary is: ', data3)
data4 = data3.values()  # Getting values in dict to a new variable
print('Values after getting in to new variable: ', data4)
list1 = list(data4)     # converting data4 in to list which is in tuple type
print('After converting in to list,: ', list1)
max_num = list1[0]      # comparing each index with each element
for each in list1:
    if each > max_num:
        max_num = each
print('The maximum number in the given values is: ', max_num)
print("______________________________________________________________")


'''
Finding max num in dictionaries using for loop
'''
data5 = {'a': 90, 'b': 13, 'c': 5, 'e': 67, 'f': 30}
print('Given Dictionary is: ', data5)
data6 = data5.values()
print('Values after getting in to new variable: ', data6)
list2 = list(data6)
print('After converting in to list,: ', list2)
min_num = list2[0]
for each in list1:
    if each < min_num:
        min_num = each
print('The maximum number in the given values is: ', min_num)
print("______________________________________________________________")


'''
Using max funx and min funx
'''
score = {'a': 44, 'b': 17, 'c': 53, 'e': 27, 'f': 83}
print(score)
large = max(score, key=score.get)
print(large)
small = min(score, key=score.get)
print(small)
