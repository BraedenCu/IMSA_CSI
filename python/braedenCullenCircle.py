from graphics import *
from random import randrange
import time


#top left 0,0. Bottom right 500, 500
class Circle:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        c = Circle(Point(50, 50), 50)
    
    
def main():
    x = Circle(20, 20)
    #x.setRandColor()
    #x.travelAccross()

if __name__=="__main__":
    main()



def setRandColor(self):
    color = color_rgb(randrange(256), randrange(256), randrange(256))
    self.c.setFill(color)

def travelAccross(self):
    c.draw(win)
    for i in range(1, 401):
        c.move(0, 1)
        time.sleep(0.001)
    win.getMouse()
    for i in range(1, 401):
        c.move(1, 0)
        time.sleep(0.001)
    win.getMouse()
    for i in range(1, 401):
        c.move(0, -1)
        time.sleep(0.001)
    win.getMouse()
    for i in range(1, 401):
        c.move(-1, 0)
        time.sleep(0.001)
    win.getMouse()
    win.close()
