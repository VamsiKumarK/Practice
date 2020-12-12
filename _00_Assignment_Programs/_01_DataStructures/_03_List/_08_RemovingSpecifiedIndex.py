'''
Created on Nov 13, 2019

@author: Vamsi
'''

'''
removing specified index in a list and print using del function
'''

data = ['Python', [1, 2, 3, 5], True, 'john']
print('Given list is: ', data)
del data[1][3]        # Removing 3rd element in second index
print('Updated data is:', data)
print('______________________')

'''
removing specified index in a list and print using remove method
'''

data = ['Python', [1, 2, 3, 5], True, 'john']
print('Given list is: ', data)
data.remove('john')
print('Updated data is:', data)


'''
we can use pop method to remove data.pop()
'''
