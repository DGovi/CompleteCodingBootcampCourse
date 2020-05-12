# problem 1

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("smthg went wrong, there was a TypeError")
finally:
    print("easy asf boy")
    print("\n" * 10)

# problem 2

try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("you cant divide by zero buddy")
finally:
    print("all done")
    print("\n" * 10)

# problem 3:


def ask():
    while True:
        try:
            integer = int(input("please enter an integer"))
            return integer
        except:
            print("you must enter an intger you dumbfuck")
            continue
        else:
            print("you entered smthg valid, everything is good here")
            break


ask()
