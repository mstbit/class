import turtle as t


t.bgcolor('orange')
t.shape('turtle')


def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)               # Point up
    t.forward(height)        # Draw up the left side
    t.right(90)
    t.forward(40)            # width of bar, along the top
    t.right(90)
    t.forward(height)        # And down again!
    t.left(90)               # put the turtle facing the way we found it.

xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs:                 # assume xs and tess are ready
    drawBar(t, v)



# Function that draws the turtle
def drawBar(t, height, color):
   
    # Get turtle t to draw one bar
    # of height
      
    # Start filling this shape
    t.fillcolor(color)
    t.begin_fill()              
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
      
    # stop filling the shape
    t.end_fill()                 
 
# Driver Code
 
xs = [48, 117, 200, 96, 134, 260, 99]
clrs = ["green", "red", "yellow", "black",
        "pink", "brown", "blue"]
 
maxheight = max(xs)
numbers = len(xs)
border = 10
  
# Set up the window and its
# attributes
wn = t.Screen()             
wn.setworldcoordinates(0 - border, 0 - border, 
                       40 * numbers + border,
                       maxheight + border)
  
# Create tess and set some attributes
tess = t.Turtle()           
tess.pensize(3)
  
for i in range(len(xs)):
     
    drawBar (tess, xs[i],
             clrs[i])
 
wn.exitonclick()

### housekeeping
t.exitonclick()
t.mainloop()