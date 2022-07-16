# question url  https://devsnest.in/algo-challenges/generate-binary-numbers-from-1-to-n

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given a number n, generate all binary numbers with decimal values from 1 to N and return the array of binary number.

# Example 1:
# Input: 3
# Output:  1 10 11
# Explanation:  Binary numbers from 1 to 3 are 1 , 10 and 11 .

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from collections import deque


def solve(n):
    q = deque()
    q.appendleft('1')
    result  = []
    if n == 1:
        return [1]

    for i in range(n):
        elem = q.pop()
        result.append(elem)

        plus_zero = elem + '0'
        q.appendleft(plus_zero)
        plus_one = elem + '1'
        q.appendleft(plus_one)

    return result

