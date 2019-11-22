'''
Created on Nov 4, 2019

@author: Vamsi
'''
subjects = ('maths', 'physics', 'english')
students = ('tom', 'john', 'tim')
data = subjects + students
print(data)
print(len(data))
for physics in data:
    print('physics')
print(data * 4)
