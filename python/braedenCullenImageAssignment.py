#from graphics import *
import random
import time
from PIL import Image

def filterPIL(colorRGB, x, y):
    im = Image.open('resized.jpg')
    im = im.convert('RGB')
    r, g, b = im.split()
    r = r.point(lambda i: i * (colorRGB[0]/256))
    g = g.point(lambda i: i * (colorRGB[1]/256))
    b = b.point(lambda i: i * (colorRGB[2]/256))
    out = Image.merge('RGB', (r, g, b))
    out.show()

def main():
    x, y = 500, 500
    r, g, b = [int(x) for x in ((input("Please enter space separated rbg values: ")).split())]
    colorRGB = [r, g, b]
    filterPIL(colorRGB, x, y)
    
if __name__=="__main__":
    main()