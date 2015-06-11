def merge_sort(sequence):
	if (len(sequence) > 1):
		mid = (len(sequence) // 2)
		left_half = sequence[:mid]
		right_half = sequence[mid:]
		merge_sort(left_half)
		merge_sort(right_half)

		k, i, j = 0, 0, 0

		while (j < len(right_half) and i < len(left_half)):
			if (left_half[i] < right_half[j]):
				sequence[k] = left_half[i]
				i += 1
			else:
				sequence[k] = right_half[j]
				j += 1
			k += 1

		while (i < len(left_half)):
			sequence[k] = left_half[i]
			i += 1
			k += 1

		while  (j < len(right_half)):
			sequence[k] = right_half[j]
			j += 1
			k += 1
			
	return sequence