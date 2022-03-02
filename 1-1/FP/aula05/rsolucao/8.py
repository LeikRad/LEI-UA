def main():
    usrInp = input("Input:\n")
    print(isPalindrome(usrInp))


def isPalindrome(txt):
    i = len(txt)-1
    palitxt = ""
    while i >= 0:
        palitxt = palitxt + txt[i]
        i -= 1
        
    return(palitxt == txt)    

if __name__ == "__main__":
    main()