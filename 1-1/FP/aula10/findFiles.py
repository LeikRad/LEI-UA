import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)
    return


def findFiles(path, ext):
    # Complete...
    lst = os.listdir(path)
    extlst = []
    for fname in lst:
        path2 = os.path.join(path, fname)
        filename, fextension = os.path.splitext(fname)
        if os.path.isdir(path2):
            recursivelist = findFiles(path2, ext)
            for i in recursivelist:
                extlst.append(i)
        elif fextension == ext:
            extlst.append(filename+fextension)
    return extlst

def main():
    print("Testing printDirFiles('..'):")
    printDirFiles("..")

    print("\nTesting findFiles('.', '.py'):")
    lst = findFiles(".", ".py")
    print(lst)
    assert isinstance(lst, list)

    print("\nTesting findFiles('..', '.csv'):")
    lst = findFiles("..", ".csv")
    print(lst)

if __name__ == "__main__":
    main()

