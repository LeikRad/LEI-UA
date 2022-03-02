def main():
    iseven()

def iseven():
    number = int(input("O número é: "))
    test = number % 2
    
    if(test == 0):
        print("O número é par")
    else:
        print("O número é ímpar")

if __name__ == "__main__":
    main()

