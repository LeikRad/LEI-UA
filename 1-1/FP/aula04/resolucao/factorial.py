def main():
    N = int(input("Factorial de? "))
    print(fact(N))
    

def fact(n):
    assert isinstance(n, int)
    assert n >= 0
    tempI = 1
    for i in range(2,n+1):
        tempI = i * tempI
    return(tempI)        


if __name__ == "__main__":
    main()