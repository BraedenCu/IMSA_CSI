from graphics import *
from random import randrange

def randColor():
    color = color_rgb(randrange(256), randrange(256), randrange(256))
    return color

def createTaxi():
    win = GraphWin("my Window", 500, 500)
    clickList = []

    #draw taxi
    coord = win.getMouse()
    coord2 = win.getMouse()
    newRect = Rectangle(coord, coord2)
    newRect.setFill("yellow")
    newRect.draw(win)
    width = abs(coord.getX() - coord2.getX())
    height = abs(coord.getY() - coord2.getY())
    win.getMouse()
    #draw wheel
    wheel1 = Circle(Point((coord.getX()+(width/4)), (coord.getY())), (width/10))
    wheel2 = Circle(Point((coord.getX()+((3*width)/4)), (coord.getY())), (width/10))
    wheel1.setFill("black")
    wheel2.setFill("black")
    wheel1.draw(win)
    wheel2.draw(win)
    #draw window holder box
    coord3 = win.getMouse()
    roofLowerX = (coord.getX()+(width/4))
    roofLowerY = coord2.getY()
    roofUpperX = coord3.getX()
    roofUpperY = coord3.getY()
    newRect = Rectangle(Point(roofLowerX, roofLowerY), coord3)
    newRect.setFill("yellow")                                                           
    heightRoof = abs(coord2.getY() - coord3.getY())
    newRect.draw(win)
    #draw window
    coord4 = win.getMouse()
    winLength = (2/3) * (heightRoof)
    winWidth = winLength
    bottomCorner = roofLowerX + (((coord3.getX())-roofLowerX)/8)
    bottomCornerY = coord3.getY() - ((coord3.getY()-roofLowerY)/8)
    windowOne = Rectangle(Point(bottomCorner, bottomCornerY), Point((bottomCorner+winWidth), (bottomCornerY+winWidth)))
    windowOne.setFill("white")
    windowOne.draw(win)
    win.getMouse()
    #draw window number two
    bottomCorner2X = roofUpperX - (((coord3.getX())-roofLowerX)/8) - winWidth
    bottomCorner2Y = roofUpperY - (((coord3.getY())-roofLowerY)/8) 
    windowTwo = Rectangle(Point(bottomCorner2X, bottomCorner2Y), Point((bottomCorner2X+winWidth), (bottomCorner2Y+winLength)))
    windowTwo.setFill("white")
    windowTwo.draw(win)
    win.getMouse()
    #write taxi
    win.setBackground("purple")
    taxiText = Text(Point((coord.getX() + (width/2)), (coord.getY() - (height/2))), "Taxi")
    taxiText.setSize(30)
    taxiText.draw(win)
    taxiText2 = Text(Point(250, 50), "I made this taxi with five clicks!! Hope you like my TAXI. Click anywhere to close the window.")
    taxiText2.draw(win)
    win.getMouse()
    
if __name__=="__main__":
    createTaxi()