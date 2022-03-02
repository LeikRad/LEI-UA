from bisect import bisect_right

def main():
    lst = []
    filetext = open("wordlist.txt", "r")

    for i in filetext: 
        lst.append(i.strip("\n"))
        
    res = BinarySearch(lst,"eb") - BinarySearch(lst,"ea")
    print(res)
    print(lst[BinarySearch(lst,"tb")])
    print(lst[BinarySearch(lst,"tb")][1])

def BinarySearch(a, x):
    i = bisect_right(a, x)
    if i:
        return (i)
    else:
        return -1

main()  