import sys
import getopt

def main():
    Alph = {}
    f1 = None
    argv = sys.argv[1:]
    
    try:   
        opts, args = getopt.getopt (argv, "f:", [ "file=" ])   
    except:   
        print("Error in Arg denotation, use -f or --file before file")

    for opt , arg in opts:   
        if opt in ['-f', '--first_file'] :   
            f1 = arg
    
    count(f1, Alph)
    showLst(Alph)

def count(fname, Alph):

    Filetxt = open(fname, mode="r", encoding="utf-8").read().lower()
    for i in Filetxt:
        if i.isalpha():
            if i in Alph:
                Alph[i] += 1
            else:
                Alph[i] = 1
    return(Alph)

def showLst(lst):
    message = "{} : {}"
    for x in sorted(list(lst), key=lambda x: lst[x], reverse=True):
        print(message.format(x, lst[x]))

if __name__ == "__main__":
    main()