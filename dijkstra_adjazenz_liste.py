from collections import defaultdict


class KnotenMitDistanz:
    def __init__(self, name: int, abstand: int) :
        self.name = name
        self.abstand = abstand


class Graph:
    def __init__(self, knoten_anzahl: int):
        self.adjazenzListe = defaultdict(list)
        self.anzKnoten = knoten_anzahl

    def addKnoten(self, src: int, knotenMitDistanz: KnotenMitDistanz):
        self.adjazenzListe[src].append(knotenMitDistanz)

    def Dijkstras_Shortest_Path (self, source: int):
        abstand = [float("inf")] * self.anzKnoten
        vorgaenger = [None] * self.anzKnoten
        abstand[source] = 0

        # Create a dictionary of { node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length:

            # Get the key for the smallest value in the dictionary
            # i.e Get the node with the shortest distance from the source
            u = min(dict_node_length, key=lambda k: dict_node_length[k])
            del dict_node_length[u]

            for node_dist in self.adjazenzListe[u]:
                adjnode = node_dist.name
                length_to_adjnode = node_dist.abstand

                # Edge relaxation
                if abstand[adjnode] > abstand[u] + length_to_adjnode :
                    abstand[adjnode] = abstand[u] + length_to_adjnode
                    dict_node_length[adjnode] = abstand[adjnode]
                    vorgaenger[adjnode] = u

        return abstand, vorgaenger


def main():
    graph = Graph(9)

    graph.addKnoten(0, KnotenMitDistanz(1, 4))
    graph.addKnoten(0, KnotenMitDistanz(7, 8))

    graph.addKnoten(1, KnotenMitDistanz(0, 4))
    graph.addKnoten(1, KnotenMitDistanz(2, 8))
    graph.addKnoten(1, KnotenMitDistanz(7, 11))

    graph.addKnoten(2, KnotenMitDistanz(1, 8))
    graph.addKnoten(2, KnotenMitDistanz(3, 7))
    graph.addKnoten(2, KnotenMitDistanz(5, 4))
    graph.addKnoten(2, KnotenMitDistanz(8, 2))

    graph.addKnoten(3, KnotenMitDistanz(2, 7))
    graph.addKnoten(3, KnotenMitDistanz(4, 9))
    graph.addKnoten(3, KnotenMitDistanz(5, 14))

    graph.addKnoten(4, KnotenMitDistanz(3, 9))
    graph.addKnoten(4, KnotenMitDistanz(5, 10))

    graph.addKnoten(5, KnotenMitDistanz(2, 4))
    graph.addKnoten(5, KnotenMitDistanz(3, 14))
    graph.addKnoten(5, KnotenMitDistanz(4, 10))
    graph.addKnoten(5, KnotenMitDistanz(6, 2))

    graph.addKnoten(6, KnotenMitDistanz(5, 2))
    graph.addKnoten(6, KnotenMitDistanz(7, 1))
    graph.addKnoten(6, KnotenMitDistanz(8, 6))

    graph.addKnoten(7, KnotenMitDistanz(0, 8))
    graph.addKnoten(7, KnotenMitDistanz(1, 11))
    graph.addKnoten(7, KnotenMitDistanz(6, 1))
    graph.addKnoten(7, KnotenMitDistanz(8, 7))

    graph.addKnoten(8, KnotenMitDistanz(2, 2))
    graph.addKnoten(8, KnotenMitDistanz(6, 6))
    graph.addKnoten(8, KnotenMitDistanz(7, 7))

    abstand, vorgaenger = graph.Dijkstras_Shortest_Path(0)
    print(f"{abstand=}")
    print(f"{vorgaenger=}")


if __name__ == "__main__":
    main()
