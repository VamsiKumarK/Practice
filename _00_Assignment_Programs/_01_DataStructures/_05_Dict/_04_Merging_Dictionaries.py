'''
Created on Nov 19, 2019

@author: Vamsi
'''

'''
merging two dictionaries
'''

data1 = {'name': 'Smith',
         'matches': 21,
         'runs': [211, 133, 98, 170],
         'avg': 96.4}
print('Details of Batsman Smith: ', data1)
data2 = {'player': 'kohli',
         'played': 33,
         'scored': [51, 73, 68, 70],
         'perf': 66.4}
print('Details of Batsman Kohli: ', data2)

data1.update(data2)
print('Details of both batsmen are: ', data1)
for each in data1.items():
    print(each)
