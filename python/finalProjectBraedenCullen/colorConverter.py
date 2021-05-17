#Sources:
#https://stackoverflow.com/questions/36434905/processing-an-image-to-sepia-tone-in-python
#https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
#https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
#https://stackoverflow.com/questions/41354948/passing-variables-to-html-file-on-python
#https://docs.python.org/3/library/webbrowser.html
#http://www.cs.uky.edu/~keen/help/Zelle-graphics-reference.pdf


from tkinter.constants import W
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
    
def convertPointillism(image, name, win):
    #convert to dot thing
    #iterate over every pixel and use the color conversion formula
    i=0
    while (i < 20000):
        x = randrange(0, image.getWidth())
        y = randrange(0, image.getHeight())
        r, g, b = image.getPixel(x, y)
        circ = Circle(Point(x, y), 2)
        circ.setFill(color_rgb(r, g, b))
        circ.draw(win)
        i+=1
    win.getMouse()
    #win.save(str("savedConvertedImages/" + "converted" + '4' + name))
    return None

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

def customPage(styling):
    #ask user style questions, then display webpage using these responses. 
    #https://stackoverflow.com/questions/41354948/passing-variables-to-html-file-on-python
    htmlCode = open("base.html").read().format(firstImage="savedConvertedImages/converted0.gif", secondImage="savedConvertedImages/convertedSave.gif", 
        thirdImage="savedConvertedImages/converted2.gif", fourthImage="savedConvertedImages/converted3.gif", 
        fifthImage="savedConvertedImages/converted4.gif")
    f = open('summary.html', 'w')
    f.write(htmlCode)   
    f.close()
    webbrowser.open('summary.html')


def userChooseOptions(imageArr, it):
    print("""
    Please enter what number based on the action you would like this program to perform on your images:
    type 1 to convert a random image to sepia
    type 2 to convert an image to black and white
    type 3 to convert an image to pointillism
    type 4 to convert an image to green filter
    type 5 to display a custom page with your images  """)
    
    userInput = eval(input("Please enter your value here: "))

    image, name = getImage(imageArr)

    if userInput == 1: 
        win1 = GraphWin(str(name + ": " + "Sepia Colorscheme"), 500, 500)
        convertedImage = convertSepia(image)
        convertedImage.draw(win1)
        #save file
        convertedImage.save(str("savedConvertedImages/" + "converted" + str(it) + '.gif'))
        win1.getMouse()
        
    elif userInput == 2:
        win2 = GraphWin(str(name + ": " + "Black and White Colorscheme"), 500, 500)
        convertedImage = convertBW(image)
        convertedImage.draw(win2)
        #save file
        convertedImage.save(str("savedConvertedImages/" + "converted" + str(it) + '.gif'))
        win2.getMouse()

    elif userInput == 3:
        win4 = GraphWin(str(name + ": " + "Pointillism Colorscheme"), 500, 500)
        convertedImage = convertPointillism(image, name, win4)

    elif userInput == 4:
        win5 = GraphWin(str(name + ": " + "Green Filter Colorscheme"), 500, 500)
        convertedImage = convertGreenFilter(image)
        convertedImage.draw(win5)
        #save file
        convertedImage.save(str("savedConvertedImages/" + "converted" + str(it) + '.gif'))
        win5.getMouse()

    elif userInput == 5:
        customPage(image)

    else:
        print("please enter a valid number.")

def main():
    while True:
        imgArr = ["image1.gif", "image2.gif", "image3.gif", "image4.gif", "image5.gif", "image6.gif", "image7.gif"]
        it = 0
        userChooseOptions(imgArr, it)
        it+=1
    
if __name__=="__main__":
    main()