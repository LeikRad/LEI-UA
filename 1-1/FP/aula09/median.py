lst = [1,2,3,4,5,6,7]
lst2 = [7,6,5,3,2,1]
lst3 = [1,2,3,6,7,10]
lst4 = [1,2,3,4,5,6,7,8,9]
lst5 = [1,2,4,5,6]

med = lambda x: sorted(x)[int(len(x)/2)] if len(x)%2 != 0 else (sorted(x)[int(len(x)/2)]+sorted(x)[(int(len(x)/2))-1])/2


print(med(lst))
print(med(lst2))
print(med(lst3))
print(med(lst4))
print(med(lst5))