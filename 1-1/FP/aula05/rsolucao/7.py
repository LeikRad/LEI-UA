def main():
    usrInp = input("Input?\n")
    print(shorten(usrInp))

def shorten(txt):
    i = 0
    shortTxt = ""
    while i < len(txt):
        if txt[i].isupper():
            shortTxt = shortTxt + txt[i]
        i += 1
    return shortTxt
        
if __name__ == "__main__":
    main()