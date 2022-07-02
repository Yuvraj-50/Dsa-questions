# question instruction :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# given an array find that the array is sorted or not using recurstion 

# examples 

# examples : 1;
# input [1 , 2 , 3] ===>> True
# input [3 , 5, 1] ===>> False

# solution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def sortedOrNot(arr):
    return helper(arr , 0)

def helper(arr , index):
    if index == len(arr) - 1:
        return True
    return arr[index] <= arr[index + 1] and helper(arr , index + 1)


h = sortedOrNot([1, 2,4, 4])  # == > True
print(h)