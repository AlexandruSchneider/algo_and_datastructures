class Knoten():
    def __init__(self, data):
        self.data = data
        self.kanten = []


def Alle_Kanten_Adjazenzliste(A: list):
    # Alternativ würde die for-Schleife besser so:
    # for i in A:
    for i in range(0, len(A)):
        for j in range(0, len(A[i].kanten)):
            el = A[i].kanten[j]
            print(f"Knoten: {A[i].data} mit Kante zu: {el.data}")


def main():
    # Einzelne Knoten erstellt
    knoten1 = Knoten(1)
    knoten2 = Knoten(2)
    knoten3 = Knoten(3)
    knoten4 = Knoten(4)

    # Knoten verbinden
    knoten1.kanten = [knoten2, knoten3]
    knoten3.kanten = [knoten2]
    knoten4.kanten = [knoten3, knoten4]

    # Adjazenzliste erstellen
    adjazenzliste = [knoten1, knoten2, knoten3, knoten4]

    Alle_Kanten_Adjazenzliste(adjazenzliste)


if __name__ == "__main__":
    main()
