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