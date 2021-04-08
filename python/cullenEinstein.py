
def numberValidation(number):
    if 100 > number or number > 999:
        print("Please enter a valid 3 digit number")
        return False 
    digit1 = number%10
    digit3 = number//100
    if abs(digit1-digit3) < 2:
        print("Please enter a valid 3 digit number")
        return False
    return True

def computeSum(number):
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
        except ValueError:
            print("Please input a valid number")
        correctInput = numberValidation(userNumber)
    computeSum(userNumber)

if __name__ == "__main__":
    main()