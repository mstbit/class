import turtle as t
import time



def sunflower(color,length,degree):

    t.fillcolor()
    # t.color("red")
    while True:
    
        t.color(color)
        t.forward(length)
        t.left(degree)
        if abs(t.pos()) <1:
            break
    
    time.sleep(5)
    # t.clearscreen()
    t.exitonclick()
    t.mainloop()
    
sunflower('red', 200, 170)