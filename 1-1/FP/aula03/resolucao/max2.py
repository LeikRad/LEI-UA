def main():
    x1 = int(input("x1? "))
    x2 = int(input("x2? "))
    print(max2(x1, x2))

def max2(x1, x2):
    if (x1 > x2):
        mx = x1
    else:
        mx = x2
    return(mx)

if __name__ == "__main__":
    main()
