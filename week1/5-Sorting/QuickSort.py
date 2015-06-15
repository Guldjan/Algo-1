def quick_sort(sequence):
	quick_sort_helper(sequence, 0, len(sequence) - 1)
	return sequence


def quick_sort_helper(sequence, first, last):
	if (first < last):
		split = partition(sequence, first, last)

		quick_sort_helper(sequence, first, split - 1)
		quick_sort_helper(sequence, split + 1, last)


def partition(sequence, first, last):
	pivot = sequence[first]
	left = first + 1
	right = last

	done = False
	while (not done):
		while (left <= right and sequence[left] <= pivot):
			left += 1
		while  (left <= right and sequence[right] >= pivot):
			right -= 1

		if right < left:
			done = True
		else:
			a = sequence[right]
			sequence[right] = sequence[left]
			sequence[left] = a

	a = sequence[right]
	sequence[right] = sequence[first]
	sequence[first] = a

	return right