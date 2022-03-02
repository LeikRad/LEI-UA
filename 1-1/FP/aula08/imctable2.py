def main():
    print(lastmanstanding([3,4,1,6,2,5,7], 3))
    print(lastmanstanding([6,3,8,2,1,8,5,2,2], 10))
    print(lastmanstanding(["Andre", "Rui", "Silva", "Madalena", "Leonor", "Francisco", "Flomena"], 7))
    print(lastmanstanding([0.5, -2, 10, 5, 8.9, 10, 20, 10], 3))
    print(lastmanstanding(["I","II","III"], 6))
    
def lastmanstanding(lst,step):
    if len(lst) == 1:
        return lst
    else:
        templst = []
        y = len(lst)
        x = step%y
        if step > y:
            x = step%y
            if x == 0:
                del lst[y-1]
                templst.extend(lst[y-1:])
                templst.extend(lst[:y-1])
            else:
                del lst[x-1]
                templst.extend(lst[x-1:])
                templst.extend(lst[:x-1])
        elif step == y:
            templst.extend(lst[:(step-1)])
        else:
            templst.extend(lst[step:])
            
            templst.extend(lst[:(step-1)])
        print(templst)
        return lastmanstanding(templst, step)



if __name__ == "__main__":
    main()