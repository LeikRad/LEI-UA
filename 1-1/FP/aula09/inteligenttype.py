from bisect import bisect_left, bisect_right
import string

def main():
    lst = []
    filetext = open("wordlist.txt", "r")
    for i in filetext: 
        lst.append(i.strip("\n"))

    while True:
        strinput = input("Starting letter?").lower()
        possLetters = BinarySearch(lst, strinput)
        if len(possLetters) == 0:
            print("You wrote {}".format(strinput))
            break
        else:
            print("Possible Letters:")
            for i in possLetters:
                print(i)



def BinarySearch(a, x):
    alphabetletters = list(string.ascii_lowercase)
    possibleLetters = alphabetletters.copy()
    
   #possibleletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabetletters:
        tempx = x + i
        pos = bisect_left(a, tempx)
        #print(tempx)
        #print(pos)
        #rint(a[pos][0:len(x)])
        
        if a[pos][0:len(x)+1] != tempx:
            possibleLetters.remove(i)
            #print(possibleLetters)

    return(possibleLetters)

if __name__ == "__main__":
    main()  