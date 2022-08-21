from turtle import *

shape('turtle')
shapesize(5, 5)
width(3)
color('purple')
speed(6)

for i in range(20):
    print(i)
    for k in range(6):
        print(f'{k} ', end=' ')
        forward(150)
        left(60)
    print()
    left(18)

