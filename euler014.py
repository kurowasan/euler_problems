'''
Problem:
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

answer: 837799
besttime: 0:00:16.454942
'''
import datetime

count = 0
first = 1

def collatz(start):
    start = int(start)
    global count
    global mem
    global first
    count += 1
    
    if first:
        first = 0
    if (start == 1):
        return count
    else:
        if start < len(mem):
            return count - 1 + mem[start]

    if (start % 2 == 0):
        return collatz(start/2)
    else:
        return collatz(3 * start + 1)
        
maximum = 0
winner = 0


mem = [0]

a = datetime.datetime.now()

for i in range(1, 1000000):
    first = 1
    count = 0
    x =  collatz(i)
    mem.append(x)

    if x > maximum:
        maximum = x
        winner = i
    
b = datetime.datetime.now()
print(b - a)


print(winner)
print(x)
