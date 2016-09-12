'''
Problem:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pythagoreanTriplet(nb):
    start = 1
    
    for a in range(start, nb - start):
        for b in range(start, nb - a):
            if (a**2 + b**2) == ((nb - a - b)**2):
                return a, b, (nb - a - b)
    return 0, 0, 0

a,b,c = pythagoreanTriplet(1000)
print(a,b,c)
print(a * b * c)