'''
Created on Nov 13, 2019

@author: Vamsi
'''


'''
finding common elements in two Lists comparing length and using range
'''

data1 = [657, 456, 24, 77, 95, 34]
print('Elements in data1 are: ', data1)
data2 = [89, 33, 73, 77, 51, 34]
comm_ele = []
if len(data1) == len(data2):
    for each in range(len(data1)):
        if data1[each] == data2[each]:
            comm_ele.append(data1[each])
else:
    print("Please enter same size of lists")
print('Elements common are: ', comm_ele)
print('____________________')


'''
finding common elements in two Lists comparing length and using range
'''

data1 = [657, 456, 24, 77, 95, 34]
print('Elements in data1 are: ', data1)
data2 = [89, 33, 73, 77, 51, 34]
print('Elements in data2 are: ', data2)
data = []
for ele in data1:
    if ele in data2:
        data.append(ele)
print('Common elements in two lists are', data)
print('____________________')
'''
list comprehension
'''

data1 = [657, 456, 24, 77, 95, 34]
print('Elements in data1 are: ', data1)
data2 = [89, 33, 73, 77, 51, 34]
print('Elements in data2 are: ', data2)
data = [ele for ele in data1 if ele in data2]
# this will loop through list and checks in another list and prints ele in List
print('Common elements in two lists are', data)
