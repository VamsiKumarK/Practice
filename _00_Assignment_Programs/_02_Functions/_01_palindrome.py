'''
Created on Nov 20, 2019

@author: Vamsi
'''

'''
checking whether given string is palindrome or not using slicing
'''


def pal(word):
    if word[0::] == word[::-1]:         # it will slice from beg and ending
        print('Entered word is palindrome')
    else:
        print('Entered word is not palindrome')


pal(str(input('enter the word: ')))
print('____________________________________')

'''
using reverse function
'''


def drome(word):
    if word == ''.join(reversed(word)):  # ''.join is used to perform strings
        print('Entered word is palindrome')
    else:
        print('Entered word is not palindrome')


drome(str(input('enter the word: ')))
