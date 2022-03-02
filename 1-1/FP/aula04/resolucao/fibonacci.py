def main():
    nTerms = int(input("Número do termo? "))
    print(fibonnaci(nTerms))

def fibonnaci(n):
    X0 = 0
    X1 = 1
    i = 1
    
    if n == 0:
        return(X0)
    
    while (i <= n):
        print(X0, X1)
        X2 = X1 + X0    # 5 = 3 + 2 
        X0 = X1         # X0 = 3
        X1 = X2         # X1 = 5
        i += 1
    return(X0)


if __name__ == "__main__":
    main()