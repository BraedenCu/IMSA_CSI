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

    def setColor(self, color):
        self.c.setFill(color)
        
def main():
    win = GraphWin("my Window", 500, 500)
    win.setBackground("black")
    numStars = 300
    sizeRangeUpper = 10
    sizeRangeLower = 2
    for i in range(0, 100):
        x = CircleSimplified(randrange(0,500), randrange(0, 500), (randrange(sizeRangeLower, sizeRangeUpper)))
        x.setColor("white")
        x.c.draw(win)
    sun = CircleSimplified(100, 250, 60)
    sun.setColor("yellow")
    sun.c.draw(win)
    mercury = CircleSimplified(200, 250, 20)
    mercury.setColor("brown")
    mercury.c.draw(win)
    venus = CircleSimplified(300, 250, 30)
    venus.setColor("red")
    venus.c.draw(win)
    earth = CircleSimplified(400, 250, 35)
    earth.setColor("green")
    earth.c.draw(win)
    time.sleep(10)
    win.getMouse()

if __name__=="__main__":
    main()