# quesiton instruction :: given a number reverse the number and return the number using recustion 

# examples :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# example  1
# input :  123 
# output : 321  

# example  2 

# input : 1011
# output : 1101

# solution ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

def reverse (num):
    if num < 10:
        return num
    return int(f"{num % 10}{reverse(num // 10)}")
  

test = reverse(123)  # ===>>  321
test = reverse(2)  # ===>>  2
test = reverse(98765)  # ===>>  56789