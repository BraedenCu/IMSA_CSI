from graphics import *
from random import randrange
import time

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
        time.sleep(0.02)

def returnToCenter(CircleSimplified1, CircleSimplified2, CircleSimplified3, CircleSimplified4, win):
    for i in range(0, 20):
        CircleSimplified1.c.move(-i, -i)
        CircleSimplified2.c.move(i, -i)
        CircleSimplified3.c.move(-i, i)
        CircleSimplified4.c.move(i, i)
        time.sleep(0.02)
        
def main():
    win = GraphWin("my Window", 500, 500)
    circles = [CircleSimplified(250, 250, 50), CircleSimplified(250, 250, 50), CircleSimplified(250, 250, 50), CircleSimplified(250, 250, 50)]
    for x in circles:
        x.setRandColor()
        x.c.draw(win)
    while(True):
        fourCirclePattern(*circles, win)
        win.getMouse()
        returnToCenter(*circles, win)
        win.getMouse()

if __name__=="__main__":
    main()