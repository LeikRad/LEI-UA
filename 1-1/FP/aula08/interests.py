
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }

    print("a) Table of common interests:")
    #commoninterests = {(list(interests.keys())[x],list(interests.keys())[y]):{z for z in interests[list(interests.keys())[x]] for j in interests[list(interests.keys())[y]] if z==j} for x in range(len(interests)) for y in range(x+1,len(interests))}
    commoninterests = {(x,y):{z for z in interests[x] if z in interests[y]} for x in interests for y in interests if x<y}
    print(commoninterests) 

    print("b) Maximum number of common interests:")
    maxCI = max( len(commoninterests[x]) for x in commoninterests)
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = {x for x in commoninterests if len(commoninterests[x]) == maxCI}
    print(maxmatches)

    print("d) Pairs with low similarity:") 
    lowJaccard = [x for x in commoninterests if (len(commoninterests[x])/(len(interests[x[0]]|interests[x[1]])))<0.25]
    print(lowJaccard)


# Start program:
main()

