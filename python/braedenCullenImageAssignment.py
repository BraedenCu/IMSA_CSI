#from graphics import *
import random
import time
from PIL import Image

def filterPIL(colorRGB, x, y):
    im = Image.open('resized.jpg')
    im = im.convert('RGB')
    r, g, b = im.split()
    r = r.point(lambda i: i * 1.5)
    out = Image.merge('RGB', (r, g, b))
    out.show()

def filters(colorRGB, x, y, image):
    win = GraphWin("window", x, y)
    it = 0
    for i in range(0, x):
        for o in range(0, y):
            it+=1
            r, g, b = image.getPixel(i, o)
            r = r*(colorRGB[0]/256)
            g = g*(colorRGB[1]/256)
            b = b*(colorRGB[2]/256)
            print(it)

    #image2 = Image(Point(x/2, y/2), image)
    #image2.draw(win)
    return image

def main():
    x, y = 500, 500
    win = GraphWin("window", x, y)
    image = Image(Point(x/2, y/2), "resized.jpg")
    
    output = filters((256, 0, 0), x, y, image)
    output.draw(win)

    time.sleep(10)

def mainOther():
    filterPIL()
    
if __name__=="__main__":
    main()