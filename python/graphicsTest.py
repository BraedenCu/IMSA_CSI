from graphics import *
from random import randrange
import time

def rand_color():
    return(color_rgb(randrange(256), randrange(256), randrange(256)))

def main():
    win = GraphWin("my Window", 500, 500)
    c = Circle(Point(50, 50), 50)
    c.setFill(rand_color())
    c.move(100, 0)
    c.draw(win)
    time.sleep(1)
    c.move(0, 100)
    c.draw(win)
    win.getMouse()

if __name__=="__main__":
    main()


def travelAccross(self):
    self.c.draw(self.win)
    for i in range(1, 401):
        self.c.move(0, 1)
        time.sleep(0.001)
    self.win.getMouse()
    for i in range(1, 401):
        self.c.move(1, 0)
        time.sleep(0.001)
    self.win.getMouse()
    for i in range(1, 401):
        self.c.move(0, -1)
        time.sleep(0.001)
    self.win.getMouse()
    for i in range(1, 401):
        self.c.move(-1, 0)
        time.sleep(0.001)
    self.win.getMouse()
    self.win.close()