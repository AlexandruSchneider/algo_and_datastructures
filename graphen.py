def makeAdjazenzListe(V, E):
    resultAdjazenz = []
    for knoten1 in V:
        kanten = []
        for knoten2 in V:
            if (knoten1, knoten2) in E:
                kanten.append([knoten2])
        resultAdjazenz.append([knoten1, kanten])
    return resultAdjazenz


def printAdjazenzListe(adjazenz):
    for element in adjazenz:
        print(element[0])
    # nicht vollständig!


def makeAdjazenzMatrix(V, E):
    # Resultat Liste (2 - dimensional)
    resultAdjazenz = []
    for knoten1 in V:
        neuerKnoten = []
        for knoten2 in V:
            if (knoten1, knoten2) in E:
                neuerKnoten.append(1)
            else:
                neuerKnoten.append(0)
        resultAdjazenz.append(neuerKnoten)
    return resultAdjazenz


def printAdjazenzMatrix(adjazenz):
    iterator = 0
    print(" ", end=" ")
    for i in range(len(adjazenz)):
        print(i, end=" ")
    print("\n")
    for row in adjazenz:
        print(iterator, end=" ")
        for number in row:
            print(number, end=" ")
        print("\n")
        iterator += 1


def BFS(V, E, start):
    istBekannt = []
    abstand = []
    vorgaenger = []
    for i in range(len(V)):
        istBekannt.append(False)
        abstand.append(None)
        vorgaenger.append(None)
    abstand[0] = 0
    istBekannt[0] = True
    Q = [start]
    while Q:
        u = Q.pop(0)
        for j in V:
            if (u, j) in E and not istBekannt[j-1]:
                abstand[j-1] = abstand[V.index(u)]+1
                vorgaenger[j-1] = u
                istBekannt[j-1] = True
                Q.append(j)
    return abstand, vorgaenger


def BFS_Index_Based(V, E, start):
    istBekannt = []
    abstand = []
    vorgaenger = []
    for i in range(len(V)):
        if V[i] == start:
            abstand.append(0)
            istBekannt.append(True)
        else:
            istBekannt.append(False)
            abstand.append(None)
        vorgaenger.append(None)
    Q = [start]
    while Q:
        u = Q.pop(0)
        for j in range(len(V)):
            if (u, V[j]) in E and not istBekannt[j]:
                abstand[j] = abstand[u-1]+1
                vorgaenger[j] = u
                istBekannt[j] = True
                Q.append(V[j])
    return abstand, vorgaenger


def main():
    start = 1
    # Liste an Knoten
    V = [start, 2, 3, 4]
    # Liste an Kanten
    E = [(start, 2), (start, 3), (2, 3), (3, 4), (4, 2)]

    adjazenz = makeAdjazenzMatrix(V, E)
    printAdjazenzMatrix(adjazenz)
    abstand, vorgaenger = BFS(V, E, start)
    print(f"{abstand=}\n{vorgaenger=}\n")

    abstand, vorgaenger = BFS_Index_Based(V, E, start)
    print(f"{abstand=}\n{vorgaenger=}\n")


if __name__ == "__main__":
    main()
