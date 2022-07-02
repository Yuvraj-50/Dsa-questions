# question instruction ::::::::::::::::::::::::::::::::::::::::::::::::::::

# find if the element exits in the array or not. if it exits then return the index 

# examples :::::::: 
# example 1 :
# input : [1, 2, 3 ,4 , 5 ,6,7] , target = 1 
# output : 0

# examples 2 :
# input  : [2 ,3 ,4, 44, 66] , target = 55
# output  : = 'No element is matching '

# solutioN 1 ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
def findTarget1(arr, target , index):
  if index + 2 > len(arr):
    if arr[index] == target:
      return index
    else:
      return 'No element is matching'
  if target == arr[index]:
    return index
  else:
    return findTarget1(arr , target , index + 1)

res1 = findTarget1([1 , 2 , 666, 2 , 4 , 5, 6, 7, 8, 555, 3] , 9999, 0)
print(res1) # ==>>> 'NO element is mathcing'

# solutioN2 :::::::::::::::::::::::::::::::::::::::::::::::::::;

def findTarget2(arr , target , index):
  if index == len(arr):
    return 'No element is matching'
  if arr[index] == target:
    return index
  else:
    return findTarget2(arr , target , index + 1)
    
    
res2 = findTarget1([1 , 2 , 666, 2 , 4 , 5, 6, 7, 8, 555, 3] , 3, 0)
print(res2)  # ==>> 10