# Largest palindrome product
# Problem 4
# 
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(n):
    """ return True if n is a palindrome, else False """
    #assert isinstance(n,int), "Can only check ints for palindrome"
    s = str(n)
    return s == s[::-1]

def three_dig_prod():
    """ somewhat sorted version of:
            return ( (i * j, i, j) for i in range(999, 99, -1) for j in xrange(i, 99, -1) )
        starting with largest
    """
    for ih in xrange(900, 0, -100):
        for jh in xrange(ih, 0, -100):
            for it in xrange(90, -1, -10):
                for jt in xrange(it, -1, -10):
                    for i in xrange(9, -1, -1):
                        for j in xrange(i, -1, -1):
                            yield (ih + it + i) * (jh + jt + j), (ih + it + i), (jh + jt + j)

def findbiggest():
    pmax = 0
    for p,i,j in three_dig_prod():
        if ispalindrome(p):
            print "{} x {} = {:6} is a palindrome".format(i,j,p)
            pmax = p if p>pmax else pmax
    print pmax,"is the largest"
    return pmax

