import turtle as t

t.bgcolor('white')     # bgcolor = background color
t.shape('turtle')
t.pensize(5)

## square
t.begin_fill()
for i in range(4):
    t.color('black')
    t.forward(100)
    t.right(90)
    t.fillcolor('violet')
t.end_fill()

### circle
# t.teleport(100, 100)
t.begin_fill()
t.circle(100)
t.fillcolor('lightgreen')
t.end_fill()

### star
# t.teleport(-200, -200)
t.begin_fill()
t.right(75)
t.forward(100)
for i in range(4):
    t.right(144)
    t.forward(100)
    t.fillcolor('cyan')
t.end_fill()

t.exitonclick()
t.done()