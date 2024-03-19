import turtle as t
import time 

def forward_right_color( num_steps, degrees ):
    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(degrees)
    time.sleep(5)
    t.clearscreen()
    t.mainloop()

# forward_right_color(10, 30)


t.color('red')
t.fillcolor('yellow')
t.begin_fill()

# while True:
#     t.forward(200)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break

t.end_fill
t.mainloop()