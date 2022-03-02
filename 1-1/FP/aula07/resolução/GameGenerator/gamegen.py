def main():
    teamList = []
    resultado = {}
    tabela = {}
    print("Escreva o nome da equipa ou deixe vazio para acabar a sua lista")
    while True:
        usrInput = input("Nome da Equipa? ")
        if (usrInput == ""):
            break
        if(usrInput in teamList):
            print("A equipa já foi introduzida")
        else:
            teamList.append(usrInput)
            tabela[usrInput] = [0,0,0,0,0,0]
    matchlist = allMatches(teamList)
    print("(Equipa 1, Equipa 2)")
    
    for i in matchlist:
        print(i)
        while True:
            try:
                goal1 = int(input("Golos da Equipa 1? "))
                break
            except:
                print("Introduza um número.")
        while True:
            try:
                goal2 = int(input("Golos da Equipa 2? "))
                break
            except:
                print("Introduza um número.")
        resultado[i] = (goal1, goal2)
        if goal1 == goal2:
            for e in i:
                tabela[e][1] += 1
                tabela[e][3] += goal1
                tabela[e][4] += goal2
                tabela[e][5] += 1
        elif goal1 > goal2:
            tabela[i[0]][0] += 1
            tabela[i[0]][3] += goal1
            tabela[i[0]][4] += goal2
            tabela[i[0]][5] += 3
            tabela[i[1]][2] += 1
            tabela[i[1]][3] += goal2
            tabela[i[1]][4] += goal1
        else:
            tabela[i[1]][0] += 1
            tabela[i[1]][3] += goal2
            tabela[i[1]][4] += goal1
            tabela[i[1]][5] += 3
            tabela[i[0]][2] += 1
            tabela[i[0]][3] += goal1
            tabela[i[0]][4] += goal2
    showTabela(tabela)

def allMatches(LST):
    MatchList = []
    i=0
    while (i < len(LST)):
        x=0
        while(x < len(LST)):
            if(LST[i] == LST[x]):
                x += 1
                continue
            match = (LST[i], LST[x])
            MatchList.append(match)
            x += 1
        i += 1 
    return(MatchList)

def showTabela(table):
    print("{:^15s} | {:^15s} | {:^15s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Equipa","Vitórias","Empates","Derrotas","Golos marcados","Golos Sofridos","Pontos"))
    message = "{:^15s} | {:^15d} | {:^15d} | {:^15d} | {:^15d} | {:^15d} | {:^15d}"
    sortedTable = sorted(table.items(), key=lambda x:x[1][5], reverse=True)
    highestTeam = [("placeholder",0)]
    for i in sortedTable:
        print(message.format(i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5]))
        if i[1][5] > highestTeam[0][1]:
            highestTeam = [(i[0],i[1][5],i[1][3],i[1][4])]
        elif i[1][5] == highestTeam[0][1]:
            highestTeam.append((i[0],i[1][5],i[1][3],i[1][4]))
    if len(highestTeam) == 1:
        print("O campeão é a equipa {}!".format(highestTeam[0][0]))
    else:
        highgoaldiff = [0,0]
        for i in highestTeam:
            teamgoaldiff = i[2]-i[3]
            if teamgoaldiff > highgoaldiff[0]:
                highgoaldiff = [teamgoaldiff, i[0]]
        print("O campeão é a equipa {}!".format(highgoaldiff[1]))

if __name__ == "__main__":
    main()