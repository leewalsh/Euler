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
