
#Program 1 - Temperature Conversion
def convertToCelcius(F):
    return (F-32)*(5/9)

#Problem 2
def printStrangeFace(numTimes):
    for i in range(0, numTimes):
        return("""\t\  |  /\n\t @   @\n\t   *\n\t \***/ \n""")


#Problem 3
def printBoxedColor(color, width, height):
    color = color + " "
    for j in range(0, height):
        if (j==0) or (j==height-1):
            print(color*(width-1))
        else:
            print(color + (" "*((width-3)*(len(color)))) + color)

#problem 4
def performAnswerProcessing(answer):
    if answer=="yes":
        return "That is great!"
    elif answer=="no":
        return "Incorrect answer."
    else:
        return "Please enter a valid answer."

def main():
    temp = input("temperature in farenheight ")
    try:
        print(convertToCelcius(float(temp)))
    except ValueError:
        print("Please input a valid temperature")
    print("\n")
    print(printStrangeFace(1))
    favColor = input("Enter your favorite color: ")
    print("\n")
    printBoxedColor(favColor, 10, 4)
    answer = input("Do you enjoy coding in Python? ")
    print("\n")
    print(performAnswerProcessing(answer))

if __name__ == "__main__":
    main()