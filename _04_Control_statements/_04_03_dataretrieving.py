'''
Created on Nov 5, 2019

@author: Vamsi
'''
'''
Retrieving data in dictionary nested for loops
'''

pl_data = {'jersey': 33,
           'name': 'Watto',
           'runs': [183, 125, 175, 121],
           'team': 'Australia'
           }
for key, val in pl_data.items():
    if key == 'name':
        for each in pl_data[key]:
            print(each)
        print('-------')
    elif key == 'team':
        for each in pl_data[key]:
            if each == 't':
                print(pl_data[key].index(each))
    elif key == 'runs':
        test = pl_data[key][2]
        print('highest score in test is ', test)
    else:
        print(pl_data[key])
    print('---')
