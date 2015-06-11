def selection_sort(sequence):
	l = len(sequence)
	for i in range(l - 1):
		minimal = i
		for j in range(i + 1, l):
			if (sequence[j] < sequence[minimal]):
				minimal = j
		if (minimal != i):
			a = sequence[i]
			sequence[i] = sequence[minimal]
			sequence[minimal] = a
	return sequence
