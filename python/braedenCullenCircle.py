from graphics import *
from random import randrange
import time


#top left 0,0. Bottom right 500, 500
class CircleSimplified:
    def __init__(self, x, y, radius): 
        self.x = x
        self.y = y
        self.radius = radius
        self.c = Circle(Point(x, y), radius)
    
    def setRandColor(self):
        color = color_rgb(randrange(256), randrange(256), randrange(256))
        self.c.setFill(color)
    
def fourCirclePattern(CircleSimplified1, CircleSimplified2, CircleSimplified3, CircleSimplified4, win):
    win.getMouse()
    for i in range(0, 20):
        CircleSimplified1.c.move(i, i)
        CircleSimplified2.c.move(-i, i)
        CircleSimplified3.c.move(i, -i)
        CircleSimplified4.c.move(-i, -i)
        time.sleep(0.01)

def returnToCenter(CircleSimplified1, CircleSimplified2, CircleSimplified3, CircleSimplified4, win):
    for i in range(0, 20):
        CircleSimplified1.c.move(-i, -i)
        CircleSimplified2.c.move(i, -i)
        CircleSimplified3.c.move(-i, i)
        CircleSimplified4.c.move(i, i)
        time.sleep(0.01)
        
def main():
    win = GraphWin("my Window", 500, 500)
    w = CircleSimplified(250, 250, 50)
    x = CircleSimplified(250, 250, 50)
    y = CircleSimplified(250, 250, 50)
    z = CircleSimplified(250, 250, 50)
    circles = [CircleSimplified(250, 250, 50), CircleSimplified(250, 250, 50), CircleSimplified(250, 250, 50), CircleSimplified(250, 250, 50)]
    x.setRandColor()
    w.setRandColor()
    y.setRandColor()
    z.setRandColor()
    for x in circles:
        x.setRandColor()
        x.c.draw(win)
    x.c.draw(win)
    w.c.draw(win)
    y.c.draw(win)
    z.c.draw(win)
    while(True):
        fourCirclePattern(w, x, y, z, win)
        win.getMouse()
        returnToCenter(w, x, y, z, win)
        win.getMouse()


if __name__=="__main__":
    main()