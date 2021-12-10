import random

def roll(c,n):
    total = 0
    for i in range(c):
        total += random.randint(1,n)
    
    return(total)
