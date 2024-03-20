import turtle as t
from random import random

for i in range(20):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
    if 0 <= angle <= 90:
        t.bgcolor("red")
    elif 90 < angle <= 180:
        t.bgcolor("blue")
    elif 180 < angle <= 270: 
        t.bgcolor("orange")
    else:
        t.bgcolor("black")

t.home()
t.exitonclick()
t.mainloop()        ### t.done()