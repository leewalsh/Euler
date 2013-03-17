
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from numpy import sqrt

def factors(n):
    """ returns generator of factors of n
        in decreasing order
        excludes n and 1 """
    return ( i for i in xrange(1 + n/2, 1, -1) if n%i==0 and i!=n)

def isprime(p):
    if p==1:
        return False
    if p==2:
        return True
    try:
        factors(p).next()
        return False
    except StopIteration:
        return True
    #alternatively:
    #return not list(factors(p))

def n_primes(n):
    """ return generator for all primes under n"""
    return ( p for p in xrange(n,2,-1) if isprime(p) )

def reduced_factors(n):
    """ returns generator of *odd* factors of n
        in decreasing order
        excludes n and 1 """
    primes = n_primes(int(n**.2))
    for p in primes:
        while n%p == 0:
            n /= p
    print 'n is now:',n
    return factors(n)
        
def biggestprime(n):
    print 'looking for biggest prime factor of',n
    for f in reduced_factors(n):
        if isprime(f):
            print f,'is prime'
            return f
