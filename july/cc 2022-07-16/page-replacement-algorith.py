# question url  :: https://devsnest.in/algo-challenges/page-replacement-algorithms

# question instruciton ::::::::::::::::::::::::::::::::::::::::::::::::::::

# In operating system, Page replacement algorithm are responsible to decide which page is needed to be replaced when new page comes in.

# Whenever a new page is referred and not present in memory, page fault occurs and Operating System replaces one of the existing pages with newly needed page.

# Given an array of integers pages of size n and a memory capacity capacity, return the total number of page faults.

# examples ;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Input:  6
#         1 3 0 3 5 6 
#         3
# Output: 5

# /solutioN :::::::::::::::::::::::::::::::::::::::::::::;;;;

from typing import Deque

def solve(n, pages, capacity):
    fifo = Deque()
    fifo_set = set()
    pages_fault = 0

    for page in pages:
        if page not in fifo_set:
            pages_fault += 1
            if len(fifo_set) == capacity:
                el = fifo.pop()
                fifo_set.remove(el)
            fifo.appendleft(page)
            fifo_set.add(page)

    return pages_fault