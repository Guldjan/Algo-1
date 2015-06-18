class Sorting:
	def selection_sort(self, sequence):
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



	def merge_sort(self, sequence):
	    if (len(sequence) > 1):
		    mid = (len(sequence) // 2)
		    left_half = sequence[:mid]
		    right_half = sequence[mid:]
		    self.merge_sort(left_half)
		    self.merge_sort(right_half)

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


	def insertion_sort(self, sequence):
	    for i in range(1, len(sequence)):
		    j = i
		    while (j > 0 and sequence[j-1] > sequence[j]):
			    a = sequence[j]
			    sequence[j] = sequence[j-1]
			    sequence[j-1] = a
			    j -= 1
	    return sequence


	def quick_sort(self, sequence):
	    self.quick_sort_helper(sequence, 0, len(sequence) - 1)
	    return sequence


	def quick_sort_helper(self, sequence, first, last):
	    if (first < last):
		    split = self.partition(sequence, first, last)

		    self.quick_sort_helper(sequence, first, split - 1)
		    self.quick_sort_helper(sequence, split + 1, last)


	def partition(self, sequence, first, last):
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