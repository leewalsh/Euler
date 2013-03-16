
# Multiples of 3 and 5
# Problem 1
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

import math
import numpy as np

def mult_sum_build(factors, limit):
    a, b = factors
    i_lim = int(math.ceil(math.log(limit, min(factors))))
    j_lim = int(math.ceil(math.log(limit, max(factors))))
    ii, jj = xrange(i_lim), xrange(j_lim)
    multiples = [ a**i * b**j for i in ii for j in jj if a**i * b**j < limit ]
    print multiples
    multiples = list(set(multiples))
    print multiples
    return sum(multiples)

def mult_sum_filter(factors, limit):
    multiples = np.arange(limit)
    mask = np.any([multiples%a == 0 for a in factors], axis = 0)
    return sum(multiples[mask])

if __name__=='__main__':
    f = (3,5)
    m = 10
    if mult_sum_filter(f,m) == 23:
        m = 1000
        print mult_sum_filter(f,m)
