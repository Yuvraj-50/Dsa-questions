# question instruction :::::::::::::::::::::::::::::::::::::::::::

# Write a Python program to calculate the value of 'a' to the power 'b'

# question examples 
# input 
# a : 3
# b : 4 

# output :
# 81

# example 3 * 3 * 3 * 3 == 81

# solution  usign recusiton ::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

def pow(number , power):
  if number == 0:
    return 0
  elif power == 1 or number == 1:
    return number
  else:
    return number * pow(number  , power - 1)