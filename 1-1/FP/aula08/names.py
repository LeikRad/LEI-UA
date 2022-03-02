from os import read
import sys
import getopt

def main():

    f1 = None
    argv = sys.argv[1:]
    dic = {}   
    try:   
        opts, args = getopt.getopt (argv, "f:")   
    except:   
        print("Error in Arg denotation, use -f before file") #Usar "python ./[nome do ficheiro de python].py -f names.txt" 
    for opt , arg in opts:   
        if opt in ['-f'] :   
            f1 = arg
    readfile(f1, dic)
    dic.pop('Nome', None)
    showlist(dic)

def showlist(dic):
    messageformat = "{} : {}"
    for i in dic:
        print(messageformat.format(i, dic[i]))
 

def readfile(f1, dic):
    with open(f1, "r") as e:
        line = e.readlines()
        for i in line:
            lst = i.split()
            if lst[-1] in dic:
                dic[lst[-1]].add(lst[0])
            else:
                dic[lst[-1]] = {lst[0]}

if __name__ == "__main__":
    main()