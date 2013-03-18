# Smallest multiple
# Problem 5
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from e3 import n_primes

def prime_fs(n):
    """ return the prime factorization of n as list
        such that this gets back to n:
            n = 1
            for p in ps: n*=p
    """
    ps = []
    for p in n_primes(1 + n/2):
        while n%p == 0:
            n /= p
            ps.append(p)
    return ps if ps else [n]

def pcount(n):
    """ generate a dictionary of primes and their count for the prime factorizatio of n """
    pcount = { p:0 for p in n_primes(n) }
    fs = range(2,n+1)
    pfs = map(prime_fs, fs)

    for f, pf in zip(fs,pfs):
        for p in pf:
            pc = pf.count(p)
            if pc > pcount[p]:
                pcount[p] = pc

    return pcount

def smallest_multiple(n):
    """ returns smallest multiple of all numbers 1..n """
    m = 1
    for p,c in pcount(n).items():
        m *= p**c
    return m

if __name__ == '__main__':
    print smallest_multiple(20)

