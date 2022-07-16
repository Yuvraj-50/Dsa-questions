# question url :: https://devsnest.in/lms?id=49&slug=infix-postfix

# question instruciton :::::::::::::::::::::::::::::::::::::::::::::::


# Infix Expression :- The expression of the form a op b where an operator is written between two operands.

# Postfix Expression :- The expression of the form a b op where an operator is followed for every pair of operands.

# Given an infix expression str. Convert the given infix expression to postfix expression and return it.

# Note :- The operators + and - have same precedence. The operators \ and * have same precedence. The operator ^ have higher precedence than \ and *. The operators * and \ have higher precedence than + and -.

# examples ;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# Input :
#     a+b*(c^d-e)^(f+g*h)-i
# Output :
#     abcd^e-fgh*+^*+i-



# ṣolution ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def solve(infix):
    stack  = []
    result = []
    p = {'(' : 0 , '+' : 1, '-' : 1 , '/' : 2 , '*' : 2 , '^' : 3}

    for i in infix:
        if i == "(":
            stack.append(i)
        elif i == ")" :
            while stack and stack[-1] != "(":
                el = stack.pop()
                result.append(el)
            stack.pop()
        elif i == "+" or i == "-" or i == '/' or i == '^' or i == '*':
            while stack and p[stack[-1]] >= p[i]:
                el = stack.pop()
                result.append(el)
            stack.append(i)
        else:
            result.append(i)

    while stack :
        el = stack.pop()
        result.append(el)
    return ''.join(result)
