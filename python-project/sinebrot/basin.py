from math import exp
from cmath import sin, cos
MAX_ITER = 80

EPSILON = 0.001
SINE_SCALE = 4.0
ESCAPE_RADIUS = 8.0
   
def cubicbrot(c):
    z = c
    n = 0
    prev = EPSILON
      
    while (abs(z) <= ESCAPE_RADIUS or abs(z-1) <= ESCAPE_RADIUS or abs(z+1) <= ESCAPE_RADIUS) and n < MAX_ITER:
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
    
def sinebrot(c):
    z = c
    n = 0
    prev = EPSILON
      
    while (abs(z) <= ESCAPE_RADIUS or abs(z-1) <= ESCAPE_RADIUS or abs(z+1) <= ESCAPE_RADIUS) and n < MAX_ITER:
        f = (z*z*z)-z
        p = 3*z*z-1
        if abs(f) > SINE_SCALE + 1:
          f = f + SINE_SCALE * sin(z)
          p = p + SINE_SCALE * cos(z)
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
