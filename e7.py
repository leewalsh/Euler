
# 10001st prime
# Problem 7
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# 
# What is the 10 001st prime number?


def is_prime(p):
    if p==1:
        return False
    if p%2==0:
        return True
    for i in xrange(3,1+p/2,2):
        if p%i == 0: return False
    return True

def primes():
    yield 2
    yield 3
    n = 3
    while True:
        n += 2
        if is_prime(n):
            yield n


    

def nth_prime(n):
    ps = n_primes(2**31-1)
    for n in xrange(1, n+1):
        p = ps.next()
    return p



