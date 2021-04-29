from graphics import *
from PIL import Image
import numpy as np
import cv2

def pixelate(imagePath, outputW, outputH, pixelationW, pixelationH):
    input = cv2.imread(imagePath)
    height, width = input.shape[:2]
    temp = cv2.resize(input, (pixelationW, pixelationH), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    outputUpscaled = cv2.resize(output, (outputW, outputH), interpolation=cv2.INTER_AREA)
    return outputUpscaled


def main():
    output = pixelate('charizardPixelArt.jpg', 1000, 1000, 16, 16)
    input = cv2.imread('charizardPixelArt.jpg')
    cv2.imshow('Output', output)
    cv2.waitKey(0)

if __name__=="__main__":
    main()