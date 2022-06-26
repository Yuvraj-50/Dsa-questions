# question url :: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# question instruction::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# examples ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )


# solution:::::::::::::::::::::::::::::::::::::::::::::::::::::
def alphabet_position(text):
    lower_text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    a = list(alphabet)
    for i in lower_text:
        if i  in alphabet:
            res += str(a.index(i) + 1) + ' '
    return res.strip()