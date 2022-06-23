# question instruction ::::
# The factorial of a positive integer n is the product of all positive integers less than or equal to n.

# You’re given a number and you have to calculate it’s factorial.

# Note: Factorial of 1 = 1, Factorial of 0 = 1

# Try doing it in both recursive and iterative method

# solutION ::::::::::::::::::::::::::::::::::::::::::::::::::
def solve(n):
    if n < 1:
        return 1
    else :
        return n * solve(n - 1)
