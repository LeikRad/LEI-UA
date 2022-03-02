def main():
    usrInp = int(input())
    
    assert usrInp > 1

    div, cat = ex11(usrInp)
    print("Divisores:", div, "|| Categoria:", cat)

def ex11(n):
    div = []
    x = 0
    category = ""
    for i in range(1, n):
        if(n % i == 0):
            div.append(i)
    for i in div:
        x = x + i

    if(x == n):
        category = "Número Perfeito"
    elif(x < n):
        category = "Número Deficiente"
    else:
        category = "Número Abundante"

    return(div, category)


if __name__ == "__main__":
    main()