def main():
    teamList = []
    print("Escreva o nome da equipa ou deixe vazio para acabar a sua lista")
    while True:
        usrInput = input("Nome da Equipa? ")
        if (usrInput == ""):
            break
        if(usrInput in teamList):
            print("A equipa já foi introduzida")
        else:
            teamList.append(usrInput)
    print(allMatches(teamList))
        
def allMatches(LST):
    MatchList = []
    i=0
    while (i < len(LST)):
        x=0
        while(x < len(LST)):
            if(LST[i] == LST[x]):
                x += 1
                continue
            match = [(LST[i], LST[x])]
            MatchList.append(match)
            x += 1
        i += 1
        
    return(MatchList)

if __name__ == "__main__":
    main()