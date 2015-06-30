import math

class HeapSort:

    # Sorts a sequence of integers.

    def heap_sort(self, sequence):
    	size = len(sequence)
    	self.heapify(sequence, size)
    	end = size - 1
    	while(end > 0):
    		self.swap(sequence, 0, end)
    		self.siftdown(sequence, 0, end)
    		end -= 1
    	return sequence


    def heapify(self,sequence, i):
        p = math.floor((i - 2) / 2)
        while (p > 0):
        	self.siftdown(sequence, p, i)
        	p -= 1

    def swap(self, sequence, i, j):
        tmp = sequence[i]
        sequence[i] = sequence[j]
        sequence[j] = tmp
          

    def siftdown(self, sequence, i, size):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if (l <= (size - 1) and sequence[l] > sequence[i]):
            largest = l
        if (r <= (size - 1) and sequence[r] > sequence[largest]):
            largest = r
        if (largest != i):
            self.swap(sequence, i, largest)
            self.siftdown(sequence, largest, size)


  

h = HeapSort()
print (h.heap_sort([4,3,2,7,4,9,1,2,4]))
              