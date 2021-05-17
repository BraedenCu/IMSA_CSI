from graphics import *
from random import randrange
import time
import webbrowser

def showImage(img, text):
    win = GraphWin(text, 500, 500)
    img.draw(win)
    #win.getMouse()

def getImage(imagePathArray):
    #get one random image
    ran = randrange(0, len(imagePathArray))
    image = imagePathArray[ran]
    for c in range(0, len(image)):
        if image[c] == '.':
            if image[c+1] != 'g':
                raise "Ensure that the files are in the gif format"
            else:
                continue
    text = image
    img = Image(Point(250, 250), image)
    #showImage(img, text)
    return img, text

def convertSepia(image):
    #convert to sepia
    #iterate over every pixel and use the color conversion formula
    for i in range(0, image.getWidth()):
        for x in range(0, image.getHeight()):
            r, g, b = image.getPixel(i, x)
            #https://stackoverflow.com/questions/36434905/processing-an-image-to-sepia-tone-in-python for math formula
            uR = int(r*0.393 + g*0.769 + b*0.189)
            uG = int(r*0.349 + g*0.686 + b*0.168)
            uB = int(r*0.272 + g*0.534 + b*0.131)
            if uR > 255: uR = 255
            if uG > 255: uG = 255
            if uB > 255: uB = 255
            image.setPixel(i, x, color_rgb(uR, uG, uB))
    return image

def convertBW(image):
    #convert to black and white
    #iterate over every pixel and use the color conversion formula
    for i in range(0, image.getWidth()):
        for x in range(0, image.getHeight()):
            r, g, b = image.getPixel(i, x)
            #https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python for math formula
            uR = int((r+g+b)/3)
            uG = int((r+g+b)/3)
            uB = int((r+g+b)/3)
            if uR > 255: uR = 255
            if uG > 255: uG = 255
            if uB > 255: uB = 255
            image.setPixel(i, x, color_rgb(uR, uG, uB))
    return image
    
def convertDots():
    #convert to dots
    pass

def convertPointillism():
    #convert to point
    pass

def convertGreenFilter(image):
    #convert to black and white
    #iterate over every pixel and use the color conversion formula
    for i in range(0, image.getWidth()):
        for x in range(0, image.getHeight()):
            r, g, b = image.getPixel(i, x)
            #https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python for math formula
            uR = int(r*0.2989)
            uG = int(g*0.5870)
            uB = int(r*0.1140)
            if uR > 255: uR = 255
            if uG > 255: uG = 255
            if uB > 255: uB = 255
            image.setPixel(i, x, color_rgb(uR, uG, uB))
    return image

def customPage():
    #ask user style questions, then display webpage using these responses. 
    pass

def userChooseOptions(imageArr):
    print("""
    Please enter what number based on the action you would like this program to perform on your images:
    type 1 to convert a random image to sepia
    type 2 to convert an image to black and white
    type 3 to convert an image to dots
    type 4 to convert an image to pointillism
    type 5 to convert an image to green filter
    type 6 to display a custom page with your images  """)
    
    userInput = eval(input("Please enter your value here: "))

    win = GraphWin("Quarter Project", 500, 500)
    image, name = getImage(imageArr)

    if userInput == 1: 
        convertedImage = convertSepia(image)
        convertedImage.draw(win)
        
    elif userInput == 2:
        convertedImage = convertBW(image)
        convertedImage.draw(win)

    elif userInput == 3:
        convertedImage = convertDots(image)
        convertedImage.draw(win)

    elif userInput == 4:
        convertedImage = convertPointillism(image)
        convertedImage.draw(win)

    elif userInput == 5:
        convertedImage = convertGreenFilter(image)
        convertedImage.draw(win)

    elif userInput == 6:
        customPage(image)
    else:
        print("please enter a valid number.")
    
    win.getMouse()
    

    
def main():
    x, y = 500, 500
    imgArr = ["veryCuteDogresized.gif"]
    #win = GraphWin("Final Project", x, y)
    userChooseOptions(imgArr)
    
if __name__=="__main__":
    main()