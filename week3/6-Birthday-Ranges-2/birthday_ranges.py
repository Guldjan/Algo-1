class BinaryIndexedTree:
	def __init__(self, sequence):
		self.l = len(sequence)
		self.tree = [0 for i in range(self.l)]
		self.tree[self.l::] = sequence
		for i in range(self.l - 1, 0, -1):
			self.tree[i] = self.tree[self.left_child(i)] + self.tree[self.right_child(i)]

	def tree(self):
		return self.tree


	def root(self):
		return self.tree[1]


	def parent(self, index):
		return index // 2


	def left_child(self, index):
		return 2 * index


	def right_child(self, index):
		return 2 * index + 1


	def update(self, index, number):
		index = self.l + index
		self.tree[index] = number

		while (self.parent(index) > 0):
			self.tree[self.parent(index)] = self.tree[self.left_child(self.parent(index))] + self.tree[self.right_child(self.parent(index))]
			index = self.parent(index)


	def query(self, index):
		i = self.l + index - 1
		
		s = 0
		while (i != 1):
			if (self.right_child(self.parent(i)) == i):
				s += self.tree[self.left_child(self.parent(i))]
			i = self.parent(i)
		return s




class BirthdayRanges:

	def __init__(self, bdays):
		self.couples = [[x, bdays.count(x)] for x, i in enumerate(bdays) if bdays.count(x) != 0]
		self.days = [x[0] for x in self.couples]
		self.numbers = [x[1] for x in self.couples]
		self.tree_of_numbers = BinaryIndexedTree(self.numbers)


	def add(self, day, number_of_people):
		index = self.days.index(day)
		self.tree_of_numbers.update(index, number_of_people)


	def remove(self, day, number_of_people):
		index = self.days.index(day)
		if number_of_people > self.numbers[index]:
			self.tree_of_numbers.update(index, 0)
		else:
		    self.tree_of_numbers.update(index, -number_of_people)


	def count(self, start_day, end_day):
		pass


b = BirthdayRanges([2,3,2,2,2,3,6,7,9,9])
print (b.tree_of_numbers.tree)
print (b.couples)
print (b.numbers)
b.remove(9, 20)
print (b.tree_of_numbers.tree)