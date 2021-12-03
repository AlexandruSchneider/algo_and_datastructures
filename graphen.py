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
        print(f"[{element[0]}]:", end="")
        for ref in element[1]:
            if ref is None:
                print("--|\n")
            else:
                print(f" ->{ref}", end="")
        print(" --|\n")


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
                abstand[j-1] = abstand[u-1]+1 if abstand[u-1] is not None else None
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
                abstand[j] =  abstand[V.index(u)]+1 if abstand[V.index(u)] is not None else None
                vorgaenger[j] = u
                istBekannt[j] = True
                Q.append(V[j])
    return abstand, vorgaenger


def DFS(V, E, start):
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
        u = Q.pop()
        for v in V:
            if (u, v) in E and not istBekannt[v-1]:
                abstand[v-1] = abstand[u-1]+1 if abstand[u-1] is not None else None
                vorgaenger[v-1] = u
                istBekannt[v-1] = True
                Q.append(v)
    return abstand, vorgaenger


def DFS_Index_Based(V, E, start):
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
    Stack = [start]
    while Stack:
        u = Stack.pop(0)
        for j in range(len(V)):
            if (u, V[j]) in E and not istBekannt[j]:
                abstand[j] = abstand[V.index(u)]+1 if abstand[V.index(u)] is not None else None
                vorgaenger[j] = u
                istBekannt[j] = True
                Stack.insert(0, V[j])
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
    print(f"Breitensuche Unterricht:\n{abstand=}\n{vorgaenger=}\n")

    abstand, vorgaenger = BFS_Index_Based(V, E, start)
    print(f"Breitensuche Indexbasiert: \n{abstand=}\n{vorgaenger=}\n")

    adjazenzListe = makeAdjazenzListe(V, E)
    print("Als Adjazenzliste ausgegeben: ")
    printAdjazenzListe(adjazenzListe)

    V = [start, 2, 3, 4, 5, 6]
    E = [(start, 2), (start, 4), (start, 5), (2, 6), (3, 5), (3, 6), (4, 2), (4, 6), (6, 1), (6, 5)]
    print("Neue Werte gewählt: ")
    printAdjazenzListe(makeAdjazenzListe(V, E))

    abstand, vorgaenger = DFS(V, E, start)
    print(f"Tiefensuche Unterricht:\n{abstand=}\n{vorgaenger=}\n")

    abstand, vorgaenger = DFS_Index_Based(V, E, start)
    print(f"Tiefensuche Indexbasiert:\n{abstand=}\n{vorgaenger=}\n")


if __name__ == "__main__":
    main()
