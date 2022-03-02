def main():
    print(poly(0))
    print(poly(1))
    print(poly(2))
    print(poly(poly(1)))

def poly(x):
    result = x**2+2*x+3
    return result

if __name__ == "__main__":
    main()