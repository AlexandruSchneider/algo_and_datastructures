def convertMatrixToList(matrix: list):
    adjList = []
    for i in range(len(matrix)):
        element = [i]
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                element.append((j, matrix[i][j]))
        adjList.append(element)
    return adjList


def printAdjazenzListe(adjazenzListe: list):
    print("Adjazenz Liste:")
    for i in adjazenzListe:
        print(i[0], end="")
        for j in i:
            if isinstance(j, tuple):
                print(f" -> {j}", end="")
        print()


def convertListeZuKantenVonTripel(adjazenzListe: list) -> list:
    kanten = []
    for i in adjazenzListe:
        for j in i:
            if isinstance(j, tuple):
                kanten.append((i[0], j[0], j[1]))
    return kanten


def main():
    a = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    adjList = convertMatrixToList(a)
    print(adjList)
    printAdjazenzListe(adjList)
    vertices = convertListeZuKantenVonTripel(adjList)
    print(vertices)

if __name__ == "__main__":
    main()
