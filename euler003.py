'''
Problem:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer:
6857 from [71, 839, 1471, 6857]
Best time:
0.006s

Walkthrough:
find the smallest prime that divides the number without remain
do until the number is not divisible (equal to 1)
'''
import datetime

def findPrimeFactors(nb):
    primes = list()
    i = 2

    while nb != 1:        
        if(nb % i == 0):
            primes.append(i)
            nb = nb / i
        else:
            i += 1
    return primes

n = 600851475143

a = datetime.datetime.now()
print(findPrimeFactors(n))
b = datetime.datetime.now()
print(b - a)