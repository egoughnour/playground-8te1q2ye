from math import exp

MAX_ITER = 80

EPSILON = 0.001
   
def cubicbrot(c):
    z = c
    n = 0
    prev = EPSILON
      
    while (abs(z) <= 2 or abs(z-1) <= 2 or abs(z+1) <= 2) and n < MAX_ITER:
        f = (z*z*z)-z
        p = 3*z*z-1
        if abs(p) <= EPSILON:
            return MAX_ITER
        prev = z
        z = z - (f/p)
        if abs(z) <= EPSILON:
            return n + 1 + exp(abs(z-prev))
        if abs(z-1) <= EPSILON:
            return n + 1 + exp(abs(z-1-prev))
        if abs(z+1) <= EPSILON:
            return n + 1 + exp(abs(z+1-prev))
        n += 1
    return n
