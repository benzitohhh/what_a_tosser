import random

a = 0.5

def ex(r):
    return (1.0 - a**r) / (a**r)

def share(r):
    total = 0.0
    for i in range(1, r+1):
        total += 1.0 / (2**i) * i
    return total

def r_in_a_row(r):
    i = 0
    total = 0
    while total < r:
        i = i + 1
        t = random.randrange(0,2)
        if t:
            total += 1
        else:
            total = 0
    return i

from math import factorial
def n_choose_k(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))
