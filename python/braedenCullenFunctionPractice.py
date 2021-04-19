
def chain(x):
    s = str(x)
    while x!=1:
        if (x%2)==0:
            x=x/2
        else:
            x=(x*3)+1
        s+="-" + str(int(x))
    return s

def longestChain(start, end):
    maxi = 0
    largest = None
    for i in range(start, end):
        val = len(chain(i))
        if val >= maxi:
            maxi = val
            largest = i
    return largest

def main():
    try:
        x = int(input("Pick a number between 1 and 100: "))
        print(chain(x))
        print(longestChain(1, 100))
    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()
