import math
from turtle import *

def heart(n):
    return 15 * math.sin(n) ** 3

def heartb(n):
    return 12 * math.cos(n)-5 *\
           math.cos(2*n) -2 *\
           math.cos(3*n) -\
           math.cos(4*n)


tracer(2)
bgcolor("black")
for i in range(800):
    goto(heart(i)*15, heartb(i)*15)
    for j in range(1):
        color("red")
        hideturtle()
        goto(0,0)

done()
