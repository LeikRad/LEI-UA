
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1]) #should be lst[0]
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO']) #CSCO@12
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {} 
    for i in lst:
        if i[0] in totVol:
            totVol[i[0]] += i[6]
        else:
            totVol[i[0]] = i[6]
    return totVol

def maxValorization(lst):
    vMax = {}
    for i in lst:
        if i[1] in vMax:
            valorization =(i[5]/i[2]-1)
            if vMax[i[1]][1] < valorization:
                vMax[i[1]] = (i[0], valorization)
        else:
            valorization =(i[5]/i[2]-1)
            vMax[i[1]] = (i[0], valorization)
    return vMax

def stocksByDateByName(lst):
    dic = {}
    e = ""
    templist = {}
    for i in sorted(lst, key=lambda x:x[1]):
        if i[1] == e:
            templist[i[0]] = i
        else:
            dic[e] = templist
            e = i[1]
            templist = {i[0] : i}
    dic[e] = templist
    return dic
    

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for i in portfolio:
        val += stocks[date][i][5] * portfolio[i]
    return val

if __name__ == "__main__":
    main()
