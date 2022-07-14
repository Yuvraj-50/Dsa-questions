# quesiton url  :: https://devsnest.in/lms?id=48&slug=deck-of-cards
# quesiton instruciton :::::::::::::::::::::::::::::::::::::::::::::::

# In a deck of cards, each card has an integer written on it.

# Return 1 if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, else return 0 where:

# Each group has exactly X cards.
# All the cards in each group have the same integer.

# # examples ;:::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Example 1:
# Input: 8
#        1 2 3 4 4 3 2 1
# Output: 1
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

# solutioN :::::::::::::::::::::::::::::::::::::::::::::::::::::::;;




def gcd (a , b):
    if b ==  0:
        return a
    return gcd(b , a%b)

def solve(n , deck):
    if n == 1:
        return 0
    dic = {}

    for i in deck:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    g = dic[deck[0]]

    for i in dic.values():
        g = gcd(max(g, i) , min(g, i))

    return 1 if g>1 else 0
