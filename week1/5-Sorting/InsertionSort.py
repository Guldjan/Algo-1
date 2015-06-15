def insertion_sort(sequence):
	for i in range(1, len(sequence)):
		j = i
		while (j > 0 and sequence[j-1] > sequence[j]):
			a = sequence[j]
			sequence[j] = sequence[j-1]
			sequence[j-1] = a
			j -= 1
	return sequence
