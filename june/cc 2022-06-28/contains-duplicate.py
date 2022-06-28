# question url  :: https://devsnest.in/algo-challenges/contains-duplicate

# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Given an integer array 'nums’, return 1(true) if any value appears at least twice in the array, and return 0(false) if every element is distinct.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;

# Input:
#     4
#     1 2 3 1
# Output:
#     1

# solution :::::::::::::::::::::::::::::::::::::::::::::::::::::::;

def solve(n, arr):
    uniqueArr = list(set(arr))
    if (len(uniqueArr) == len(arr)):
        return 0
    else:
        return 1
