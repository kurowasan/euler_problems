'''
Problem:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def generatePrimeFactor(limit):
    factors = []
    for i in range(2, limit):
        nb = i
        for factor in factors:
            if(nb % factor == 0):
                nb = nb/ factor
        if(nb != 1):   
            factors.append(nb)   
    return factors

def multiply(arr):
    result = 1
    for i in range(len(arr)):
        result *= arr[i]
    return result
        
print(multiply(generatePrimeFactor(20)))