def max(arr):
    MaxSum = 0
    for i in arr:
        TempSum = i
        for x in arr:
            if i == x:
                continue
            elif TempSum+x > TempSum:
                TempSum += x
        if TempSum > MaxSum:
            MaxSum = TempSum
    return(MaxSum)
