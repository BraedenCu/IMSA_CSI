def main(start, end):
    for i in range(start, end):
        i+=1
        if i%3==0 or i%5==0:
            if i%3==0:
                if i%5==0:
                    print("fizzbuzz")
                else:
                    print("fizz")
            else:
                print("buzz")
        else:
            print(i)

main(0, 49)

