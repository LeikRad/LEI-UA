import os
from typing import List, Sized

def main():
    FLst = os.listdir()
    SLst = sizeChecker(FLst)
    show(SLst)

def sizeChecker(Dir):    
    Lst = []
    for i in Dir:
        Lst.append((i, os.stat(i).st_size))
    return(Lst)

def show(Lst):
    Divs = {0 : "Bytes",
            1 : "KiB",
            2 : "MiB",
            3 : "GiB",
            4 : "TiB",
    }
    byteDiv = 1024
    message = "File: {} Size: {:.2f} {}"

    for i in range(0,len(Lst)):
        size = float(Lst[i][1])    
        n = 0
        while size >= 1024:
            size = size / byteDiv
            n += 1
        print(message.format(Lst[i][0], size, Divs[n]))
        


if __name__ == "__main__":
    main()
