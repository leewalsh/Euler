
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

import numpy as np

def fib(s=(1,2), limit=89):
    if s[-1] < limit:
        t = sum(s[-2:])
        return fib(s + (t,))
    elif s[-1] == limit:
        print 'right on',s[-1],limit
        return np.array(s)
    elif s[-1] > limit:
        print 'went over',s[-2],limit
        return np.array(s[:-1])

def seven(s):
    s = np.asarray(s)
    return s[s%2==0].sum()


#if seven(fib(s=(1,2),limit=89)) == seven([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
print 'sum_evens:',seven(fib(s=(1,2),limit=4e6))
    
