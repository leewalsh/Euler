
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def factors(n):
    """ returns generator of all factors of n
        in decreasing order
        excludes n and 1
    """
    return ( i for i in xrange(1 + n/2, 1, -1) if n%i==0 and i!=n)

def is_prime(p):
    """ return True if p is prime, else False """
    if p==1:
        return False
    if p==2:
        return True
    try:
        factors(p).next()
        return False
    except StopIteration:
        return True

def n_primes(n):
    """ return generator for all primes under n
        in increasing order
    """
    return ( p for p in xrange(2,n,1) if is_prime(p) )

def reduced_factors(n):
    """ returns generator of *reduced* factors of n
        in decreasing order
        after dividing out several smaller primes
        excludes n and 1
    """
    cutoff = lambda n: int(n**.3)
    primes = n_primes(cutoff(n))
    pmax = 0
    for p in primes:
        while n%p == 0:
            n /= p
            pmax = p
    return pmax, n, factors(n)
        
def largest_prime_factor(n):
    p,m,fs = reduced_factors(n)
    if m > p and is_prime(m):
        return m

    for f in fs:
        if f > p and is_prime(f):
            return f
    else:
        return p

if __name__ == '__main__':
    print largest_prime_factor(600851475143)
