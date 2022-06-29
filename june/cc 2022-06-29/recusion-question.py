# Write a Python program to get the sum of a non-negative integer.

# examples 
# input : 123 ==> 1 + 2 + 3
# output : 6

# slution :::::::::::::::::::::::::::::::::::::::::::::::::::::::

def sumOfNum(num):
    if num <= 9:
        return num
    else:
        num = num % 10 + sumOfNum(num // 10)
        return num
