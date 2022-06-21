# question url:: https://devsnest.in/algo-challenges/characters-frequency

# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::

# Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.

# examples //////////////////////////////////////////////////////////////////
# Example 1:
# Input:
#     arfardarb
# Output:
#     3 3 1 1 1

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def solve(str1):
  arr = list(str1)
  unique_arr = list(dict.fromkeys(arr))
  res = []
  for i in unique_arr:
    c = arr.count(i)
    res.append(c)
  return res