def main():
    x1 = int(input("x1? "))
    x2 = int(input("x2? "))
    x3 = int(input("x3? "))
    print(max3(x1,x2, x3))

def max2(x1, x2):
    if (x1 > x2):
        mx = x1
    else:
        mx = x2
    return(mx)

def max3(x1, x2, x3):
    mxTemp = max2(x1, x2)
    mx = max2(mxTemp, x3)
    return(mx)

if __name__ == "__main__":
    main()
