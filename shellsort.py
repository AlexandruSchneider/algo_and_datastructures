def shellSort(A) -> None:
	schrittweite = 0
	while 3 * schrittweite - 1 < len(A):
		schrittweite = 3 * schrittweite + 1

	while schrittweite > 0:
		for i in range(schrittweite, len(A)):
			neu = A[i]
			k = i
			while k >= schrittweite and A[k-schrittweite] > neu:
				A[k] = A[k-schrittweite]
				k -= schrittweite
			A[k] = neu
		schrittweite = int(round(schrittweite/3, 0))

liste = [5, 19, 1, 20, 2, 18, 13, 4, 3, 11]

print(liste)

shellSort(liste)

print(liste)
