def binarySearchRek(liste, key, links, rechts):
    mitte = (links + rechts) // 2
    if links == rechts:
        print("Wert nicht in der Liste gefunden!")
        return None
    if liste[mitte] == key:
        return liste[mitte]
    elif liste[mitte] > key:
        return binarySearchRek(liste, key, links, mitte-1)
    elif liste[mitte] < key:
        return binarySearchRek(liste, key, mitte+1, rechts)


def binarySearchRekAlt(liste, key):
    mitte = len(liste) // 2
    if not liste:
        print("Wert nicht in der Liste gefunden!")
        return None
    if liste[mitte] == key:
        return liste[mitte]
    elif liste[mitte] > key:
        return binarySearchRekAlt(liste[:mitte-1], key)
    elif liste[mitte] < key:
        return binarySearchRekAlt(liste[mitte+1:], key)

listeTest = [1,4,7,8,13,15,16,17,22,29]


print(binarySearchRek(listeTest, 8, 0, len(listeTest)))
print(binarySearchRekAlt(listeTest, 8))
