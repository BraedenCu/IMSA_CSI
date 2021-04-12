import math

class Triange():
    def __init__(self, sidea, sideb, sidec):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        #semiperimeter
        self.semi = (sidea+sideb+sidec)/2
    
    def checkValid(self):
        a=self.sidea
        b=self.sideb
        c=self.sidec
        if ((a+b > c) and (b+c > a) and (c+b > a)):
            return True
        print("Please enter a valid triangle")
        return False

    def calculateArea(self):
        return round(math.sqrt(self.semi*(self.semi-self.sidea)*(self.semi-self.sideb)*(self.semi-self.sidec)), 2)


def main():
    valid = False
    while(valid==False):
        userInput = input("Enter as SPACE separated side lengths: ")
        try:
            #remove spaces from user input, then use list comprehension to convert those values to integers then store them in a list
            #to then be destrucuted into variables
            sidea, sideb, sidec = [int(x) for x in userInput.split()]
            triangle = Triange(sidea,sideb,sidec)
            valid = triangle.checkValid()
        #value error is thrown if user input cannot be cast to an integer
        except ValueError:
            print("please enter a valid number")

    x = triangle.calculateArea()
    print(x)
    
if __name__ == "__main__":
    main()