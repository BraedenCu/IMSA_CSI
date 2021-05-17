#Braeden Cullen, Ella Voyles
from graphics import *#import the graphics file
from random import randrange#import random number generator
import time#import time module
def rand_color():#function to generate a random color
    return(color_rgb(randrange(256),randrange(256),randrange(256)))
def main():
    win = GraphWin("My Window",500,500)
    #sample five numbers between 1 and 9 both inclusive and
    #add them to the list.Suppose the list has {2,4,2,5,8]
    list1 = []
    for i in range(0, 5):
        list1.append(eval(input("Input a number between 1 and 9: ")))
    print("Now you can click to draw your circles")
    radius = 100
    for i in list1:
        c = win.getMouse()
        for i in range(0, i):
            circle = Circle(Point(c.getX(),c.getY()), (radius-(10*i)))
            circle.setFill(rand_color())
            circle.draw(win)


    #At the first point of click draw 2 concentric random-colored circles.
    #At the second point of click draw 4 concentrinc random-colored circles..
    #And so on, until all circles have been drawn.
    
    win.getMouse()
    win.close()
main()
