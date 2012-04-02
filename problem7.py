import math

def isPrime(n):
    return not (n < 2 or any(n % x == 0 for x in xrange(2, int(n**0.5) + 1)))

currentMax =0
primes = 0
counter = 0

while (primes<10001):
    if (isPrime(counter)):
        currentMax = counter
        primes+=1
    counter+=1
print currentMax
