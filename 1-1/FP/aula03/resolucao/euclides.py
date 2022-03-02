def main():
    while True:
        a = input("a? ")
        if a.isdigit():
            a = int(a)
            break
            
    while True:
        b = input("b? ")
        if b.isdigit():
            b = int(b)
            break
    print(mdc(a, b))

def mdc(x1, x2):
    r = x1 % x2
    if(r == 0):
        return(x2)
    else:
        return (mdc(x2, r))

if __name__ == "__main__":
    main()

