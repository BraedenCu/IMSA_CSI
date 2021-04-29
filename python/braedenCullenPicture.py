from graphics import *
from PIL import Image
import numpy as np

def pilToNumpy(image):
    np_array = np.asarray(image)
    return np_array

def computeSquareOutput(img):
    image = pilToNumpy(img)
    x, y, z = np.shape(img)
    print(x, y)
    output = np.zeros((int(x/4), int(y/4), z))
    #iterate over width
    for i in range(0, int(x/4)):
        #itrate over length
        for j in range(0, int(y/4)):
            averageR = int((image[i][j][0]+image[i+1][j][0]+image[i][j+1][0]+image[i+1][j+1][0])/4)
            averageG = int((image[i][j][1]+image[i+1][j][1]+image[i][j+1][1]+image[i+1][j+1][1])/4)
            averageB = int((image[i][j][2]+image[i+1][j][2]+image[i][j+1][2]+image[i+1][j+1][2])/4)
            #print(averageR)
            output[int(i/4)][int(j/4)][0] = averageR
            output[int(i/4)][int(j/4)][1] = averageG
            output[int(i/4)][int(j/4)][2] = averageB
            j+=4
    i+=4
    print(np.shape(output))
    return output

def main():
    win = GraphWin("picture", 600, 600)
    im = Image.open('squidwardDude.resized.jpg')
    #im2 = im.resize((600, 600))
    output = computeSquareOutput(im)
    PIL_image = Image.fromarray(np.uint8(output)).convert('RGB')
    PIL_image.show()


if __name__ == "__main__":
    main()