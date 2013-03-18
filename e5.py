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
    return ps


