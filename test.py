import turtle as t


t.bgcolor('orange')
t.shape('turtle')

def shape(side, length):

    t.forward(length)
    t.left(360/side)


shape(3, 100)



### housekeeping
t.exitonclick()
t.mainloop()