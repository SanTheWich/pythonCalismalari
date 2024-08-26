x = 'print(55)'
eval(x)
#! Recursion function(AGHMEH)
import turtle
a=0
def tt():
    global a
    for b in range(4):
        turtle.forward(a)
        turtle.left(90)
    a+=10
    if a<110:
        tt()
    else:
        print()
tt()