
def chain(x):
    s = str(x)
    length = 1
    while x!=1:
        if (x%2)==0:
            x=x/2
        else:
            x=(x*3)+1
        length+=1
        s = s + "-" + str(int(x))
    return s, length
def longestChain(start, end):
    largest = 0
    length = 1
    for i in range(start, end):
        num, lengthm = chain(i)
        if lengthm >= length:
            largest = i
            length = lengthm
    return largest, length

def main():
    try:
        userInput = (input("Space separated indices for chain test: "))
        x, y = [int(x) for x in userInput.split()]
        largestNum, chainLength = longestChain(x, y)
        print("The largest chain is {} characters long, the number that produces this chain is {}".format(chainLength, largestNum))
    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()
