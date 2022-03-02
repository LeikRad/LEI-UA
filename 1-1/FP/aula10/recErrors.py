def firstEqualLast(lst):
    if len(lst) <= 1:
      return 0
    elif len(lst) == 2:
        if lst[0] == lst[1]:
            return 1
        else:
            return 0
    lst1sthalf = lst[0:len(lst)//2]
    if len(lst)%2 == 0:
      lst2ndhalf = lst[len(lst)//2:]
    else:
      lst2ndhalf = lst[len(lst)//2+1:]
    while len(lst1sthalf) > 1:
      if lst1sthalf == lst2ndhalf:
         return len(lst1sthalf)
      else: 
         lst1sthalf.pop()
         lst2ndhalf.pop(0)
    return 0
print(firstEqualLast([1,2,3,3,2,1]))
