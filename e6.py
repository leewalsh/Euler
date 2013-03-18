
# Sum square difference
# Problem 6
# 
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
# 

def summed_squares(n):
    """ returns the sum of the squares of the first n natural numbers """
    ns = ( i*i for i in xrange(1,n+1) )
    return sum(ns)

def squared_sum(n):
    """ returns the square of the sum of the first n natural numbers """
    s = n * (n+1) / 2
    return s * s

def sum_square_diff(n):
    return squared_sum(n) - summed_squares(n)

