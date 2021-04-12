def numberValidation(number):
    if 100 > number or number > 999:
        print("Please enter a valid 3 digit number")
        return False 
    #only need digits one and three to perform input validation
    digit1 = number%10
    digit3 = number//100
    #Ensure that the difference between the two digits is two or greater
    if abs(digit1-digit3) < 2:
        print("Please enter a valid 3 digit number")
        return False
    return True

def computeSum(number):
    #Reverse number using python list slicing syntax (super useful)
    reversedNumber = int("{}".format(number)[::-1])
    print(number, reversedNumber)
    difference = abs(number-reversedNumber)
    print(difference)
    reversedDifference = int("{}".format(difference)[::-1])
    print(reversedDifference)
    print(difference+reversedDifference)

def main():
    correctInput = False
    print("hello")
    print("\n")
    while (correctInput!=True):
        try: 
            userNumber = int(input("test"))
            correctInput = numberValidation(userNumber)
        except ValueError:
            print("test")
    computeSum(userNumber)

if __name__ == "__main__":
    main()