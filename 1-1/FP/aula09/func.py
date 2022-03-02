import math

def findZero(func, a, b, tol):
    if func(a) > 0:
        while (b-a) > tol:
            tempx = (a+b)/2
            tempy = func(tempx)
            if tempy > 0:
                a = tempx
            elif tempy < 0:
                b = tempx
            else:
                a = b = tempx
    else:
        while (b-a) > tol:
            tempx = (a+b)/2
            tempy = func(tempx)
            if tempy > 0:
                b = tempx
            elif tempy < 0:
                a = tempx
            else:
                a = b = tempx
    return[a,b]

def main():
    def f(x):
        return (x + math.sin(10*x))
    print(findZero(f,0.2,0.4,0.00001))
    print(findZero(f,0.5,0.6,0.0001))


if __name__ == "__main__":
    main()