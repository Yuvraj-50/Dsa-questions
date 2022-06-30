# question instruction ::: To check a given string is a palindorme or not using recursion . 

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# examples 1 
# input : 'aba'
# output : True

# example 2 
# input : 'hello'
# output : False 

def palindrome (string , start , end ):
    if start >= end :
        return True
    if string[start] != string[end]:
        return False
    palindrome(string , start + 1 ,end - 1);
    return True


string = 'aba'
test = palindrome(string , 0 , len(string) - 1)
print(test) # ==>> return True because it is palindrome