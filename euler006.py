'''
Problem:
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer:
25164150.0
Best Time:
0.000s

'''
import datetime

def findSquareOfSum(n):
    return ((n*(n + 1)/2) ** 2)

def findSumOfSquare(n):
    return (n*(n + 1)*(2*n + 1))/6
        
def findDiffSquare(n):
    return findSquareOfSum(n) - findSumOfSquare(n)
    

number = 100
a = datetime.datetime.now()
print(findDiffSquare(number))
b = datetime.datetime.now()
print(b - a)