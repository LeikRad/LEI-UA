import turtle

def main():
    wn = turtle.Screen()        # creates a graphics window
    test = turtle.Turtle()    
    name = input("File? ")
    if not ".txt" in name:
        name = name + ".txt"
    print(FileTurtle(test, name))

def FileTurtle(t, filename):
    with open(filename, "r") as e:
        lst = e.read().split()
        i = 0
        while i < len(lst):
            if (lst[i] == "UP"):
               t.up()
               i += 1

            if (lst[i] == "DOWN"):            
                t.down()
                i += 1
        
            if (lst[i].strip("-").isdigit()):            
                x = int(lst[i])
                y = int(lst[i+1])
                t.goto(x, y)
                i += 2

    turtle.exitonclick()
    return("Done!")  


if __name__ == "__main__":
    main()
