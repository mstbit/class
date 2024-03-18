import turtle as t


while True:
    
    t.color('red')
    t.forward(200)
    t.left(170)
    if abs(t.pos()) <1:
        break
    
time.sleep(5)
t.clearscreen()
t.mainloop()