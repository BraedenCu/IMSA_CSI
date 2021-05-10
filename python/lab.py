from graphics import *
from random import randrange
import time


def setRandColor(self):
    color = color_rgb(randrange(256), randrange(256), randrange(256))
    self.c.setFill(color)
    
def fourCirclePattern(circleList, win):
    win.getMouse()
    for i in range(0, 20):
        CircleSimplified1.c.move(i, i)
        CircleSimplified2.c.move(-i, i)
        CircleSimplified3.c.move(i, -i)
        CircleSimplified4.c.move(-i, -i)
        time.sleep(0.02)


def main():
    win = GraphWin("My Window", 500, 500)
    n1 = input("Input a number between 1 and 9: ")
    n2 = input("Input a number between 1 and 9: ")
    n3 = input("Input a number between 1 and 9: ")
    n4 = input("Input a number between 1 and 9: ")
    n5 = input("Input a number between 1 and 9: ")
    cList = [n1, n2, n3, n4, n5]
    for i in cList:
        c = win.getMouse()
        circle = Circle(Point(c.getX(),c.getY()), radius))