'''
Created on Nov 21, 2019

@author: Vamsi
'''

'''
Fibonocci series using while loop
'''

nterms = int(input("How many terms? "))


def fib(num1):
    n1, n2 = 0, 1
    count = 0
    # check if the number of terms is valid
    if num1 <= 0:
        print("Please enter a positive integer")
    elif num1 == 1:
        print("Fibonacci sequence upto", num1, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < num1:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth

            count += 1


fib(nterms)
print("______________")


'''
VERIFY AFTER BY USING RETURN STATEMENT
'''


'''
Using For Loop

terms = int(input("How many terms? "))


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        list1 = [0, 1]
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            list1.append(b)
        return list1

print(fibonacci(terms))
'''
