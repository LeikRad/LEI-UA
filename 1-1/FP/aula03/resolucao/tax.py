def main():
    print("r=500", tax(500))
    print("r=1000", tax(1000))
    print("r=1500", tax(1500))
    print("r=2000", tax(2000))
    print("r=2500", tax(2500))

def tax(r):
    if(r <= 1000):
        return(0.1*r)
    elif(r <= 2000):
        return(0.2*r - 100)
    else:
        return(0.3*r-300)

if __name__ == "__main__":
    main()