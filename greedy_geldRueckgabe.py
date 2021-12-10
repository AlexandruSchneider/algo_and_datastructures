def gierigeGeldruckgabe(frankenBetrag: float):
    rappen = int(frankenBetrag * 100)
    anzMunzen = [0]*4
    artMunzen = [1, 5, 10, 20]
    for i in range(3, -1, -1):
        anzMunzen[i] = rappen // artMunzen[i]
        rappen -= anzMunzen[i] * artMunzen[i]
    return anzMunzen


def main():
    frankenBetrag = 6.57
    anzMunzen = gierigeGeldruckgabe(frankenBetrag)
    print(f"{anzMunzen=}")
    # problem wenn z.b. eine 4er münze gibt
    # weil wenn 8 rappen gegeben werden werden eine 5er und 3 1er gegeben anstatt 2 4er


if __name__ == "__main__":
    main()

'''
Pseudocode:

################################################################
gierigeGeldrückgabe(franken)
Rückgabe: Liste mit Anzahl pro Münze
    1. rappen <- franken * 100
    2. anzMunzen <- allokiere Liste(4)
    3. artMunzen <- allokiere Liste(4)
    4. artMunzen[1] <- 1
    5. artMunzen[2] <- 5
    6. artMunzen[3] <- 10
    7. artMunzen[4] <- 20
    8. for i <- artMunzen.laenge, i <- i - 1, 1 do
    9.     anzMunzen[i] <- abrunden(rappen / artMunzen[i])
    10.    rappen <- rappen - (anzMunzen[i] * artMunzen[i])
    11.return anzMunzen
################################################################
'''