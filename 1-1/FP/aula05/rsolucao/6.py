def main():
    usrInp = input("Input?\n")
    print(countDigits(usrInp), "digitos")

def countDigits(txt):
    if txt.isdigit():
        return(len(txt))
    else:
        n = 0
        i = 0
        while i < len(txt):
            if txt[i].isdigit():
                n += 1
            i += 1
        return n
        
if __name__ == "__main__":
    main()