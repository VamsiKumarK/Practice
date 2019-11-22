'''
Created on Nov 4, 2019

@author: Vamsi
'''
'''
salary hike increment using for loop
'''

emp_data = {1234: ['madhu', 10000, 5],
            5667: ['john', 20000, 4],
            2345: ['tim', 30000, 3]
            }
for emp_id in [1234, 5667, 2345]:
    print(emp_id)
    sal = emp_data[emp_id][1]
    print('sal is', sal)
    if emp_data[emp_id][2] == 5:
        hike = sal*30/100
        print('hike is', hike)
    elif emp_data[emp_id][2] == 4:
        hike = sal*25/100
        print('hike is', hike)
    else:
        hike = sal*20/100
        print('hike is', hike)
    emp_data[emp_id][1] = sal
    sal = sal + hike
    print('updated salary is', sal)
