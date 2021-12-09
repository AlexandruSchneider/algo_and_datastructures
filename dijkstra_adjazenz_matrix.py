def dijkstra_adjazenz_matrix(V, adjazenz, start):
    abstand = [float("inf")] * V
    vorgaenger = [None] * V
    istFertig = [False] * V

    abstand[start] = 0

    for i in range(V):
        u = Naechster_Knoten_Dijkstra(V, istFertig, abstand)
        istFertig[u] = True
        for j in range(V):
            if adjazenz[u][j] > 0 and istFertig[j] is False and abstand[j] > abstand[u] + adjazenz[u][j]:
                abstand[j] = abstand[u] + adjazenz[u][j]
                vorgaenger[j] = u

    return abstand, vorgaenger


def Naechster_Knoten_Dijkstra(V: int, istFertig: list, abstand: list):
    minimumWert = float("inf")
    naechster = None
    for i in range(V):
        if abstand[i] < minimumWert and istFertig[i] is False:
            minimumWert = abstand[i]
            naechster = i
    return naechster


def main():
    adjazenz = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    abstand, vorgaenger = dijkstra_adjazenz_matrix(len(adjazenz[0]), adjazenz, 0)
    print(f"{abstand=}")
    print(f"{vorgaenger=}")


if __name__ == "__main__":
    main()
