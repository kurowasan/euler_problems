'''
Problem:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Answer:
104743
Best Time:
0.070s # with yield

with the sieve of eratosthen 
0.544s

with slowest algo:
02:39.682
'''
import datetime
from itertools import islice

# simplest algorithm, but slow....
def listAllPrimesTill(limit):
    nbPrime = 0
    isPrime = True;
    nb = 2

    while(nbPrime < limit):
        for divider in range(2, nb):
            if(nb % divider == 0):
                isPrime = False
                break;
        if(isPrime):
            nbPrime += 1
        nb += 1
        isPrime = True
        
    return (nb - 1)

def primes(limit):
    allNb = [x for x in range(0, limit)]
    allNb[1] = 0
    i = 2
    
    while i < len(allNb):
        for ii in range(i + i, len(allNb), i):
            allNb[ii] = 0
        i += 1
    allNb = list(filter((0).__ne__, allNb))
    
    return allNb[10000]
    
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False               
                
            
myLimit = 150000
a = datetime.datetime.now()
print(primes(myLimit))
b = datetime.datetime.now()
print(b - a)


def eratosthenes(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            for j in range(i*i, n+1, i):
                multiples.append(j)

a = datetime.datetime.now()
t = primes_sieve(myLimit)
print(next(islice(t, 10000, None), None))
b = datetime.datetime.now()
print(b - a)