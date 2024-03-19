import math


def height_width():
    height = input("Enter height\n")
    width = input("Enter width\n")
    return int(height), int(width)


def rectangle():
    height, width = height_width()
    if height == width:
        print("The area is: " + str(height*height) + "\n")
    else:
        print("The scope is: " + str(height*2+width*2) + "\n")


def triangle():
    height, width = height_width()
    option = input("Enter 1 to get the triangle's scope and 2 to print the triangle\n")
    # print scope
    if option == "1":
        line = math.sqrt(math.pow(height, 2) + math.pow(width, 2))
        print("The scope is: " + str((2*line)+width) + "\n")
    # invalid height or width for printing triangle
    elif width % 10 == 0 or width > height*2:
        print("Can't print triangle\n")
    # printing triangle with height 2
    elif height == 2:
        print(" "*int(width/2) + "*\n" + "*"*width)
    # printing other triangles
    else:
        lst = list(range(1, width+1, 2))
        for num in lst:
            if num == 1:
                print(" "*int(width/2) + "*")
            elif num == width:
                print("*"*num)
            else:
                print((" "*int((width-num)/2) + "*"*num + "\n")*int((height-2)/((width-3)/2)), end="")
                if num == 3:
                    print((" " * int((width - num) / 2) + "*" * num + "\n") * int((height - 2) % ((width - 3) / 2)), end="")


if __name__ == "__main__":
    val = input("enter 1 for rectangle, 2 for triangle and 3 to finish\n")
    while val != "3":
        if val == "1":
            rectangle()
        elif val == "2":
            triangle()
        else:
            print("invalid input\n")
        val = input("enter 1 for rectangle, 2 for triangle and 3 to finish\n")
    print("We are finished")
