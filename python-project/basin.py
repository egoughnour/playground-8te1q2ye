
MAX_ITER = 80

EPSILON = 0.001
   
def cubicbrot(c):
    z = c
    n = 0
    while (abs(z) <= 2 or abs(z-1) <= 2 or abs(z+1) <= 2) and n < MAX_ITER:
        f = (z*z*z)-z
        p = 3*z*z-1
        if abs(p) <= EPSILON:
            return MAX_ITER
        z = z - (f/p)
        if abs(z) <= EPSILON:
            return n
        if abs(z-1) <= EPSILON:
            return n
        if abs(z+1) <= EPSILON:
            return n
        n += 1
    return n

