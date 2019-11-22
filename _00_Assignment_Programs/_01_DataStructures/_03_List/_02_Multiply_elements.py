'''
Created on Nov 12, 2019

@author: Vamsi
'''
'''
Multiplying elements of a list
'''
result = 1          # Instialising result to zero
points = [3, 4, 44, 57, 78]
print('points: ', points)
for unit in range(0, len(points)):
    result = result * points[unit]
print('Multiplication of units in points is ', result)
print('_____________')


'''
finding maximunm number from the given list
'''
data = [3, 4, 44, 57, 78]
print('Given data is: ', data)
print('maximum number from the given data is: ', max(data))
print('_____________')

'''
Finding minimum number in the given list
'''
data = [3, 4, 44, 57, 78, 3]
print('Given data is: ', data)
print('minimum number from the given data is: ', min(data))
print('_____________')
