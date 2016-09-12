'''
Problem:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Answer:
142913828922
Best time:
1.232 s
'''
import datetime

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False    

a = datetime.datetime.now()
primes = primes_sieve(2000000)

sum = 0
for i in primes:
    sum += i
print (sum)

b = datetime.datetime.now()
print(b - a)