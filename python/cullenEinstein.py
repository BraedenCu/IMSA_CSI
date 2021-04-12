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
    print("Hello, today you will be playing the Einstein game. First, give a three digit number where the first and the last digits differ by two.")
    print("\n")
    while (correctInput!=True):
        try: 
            userNumber = int(input("Your number: "))
            correctInput = numberValidation(userNumber)
        #If casting the user input into an integer results in a ValueError, it means that the value they entered is not a valid integer. Upon which, it will run the following code
        #Which will prompt them to reenter a valid number. This cycle will repeat until the user enters a valid integer.
        except ValueError:
            print("Please input a valid number")
    computeSum(userNumber)

if __name__ == "__main__":
    main()