def birthday_ranges(birthdays, ranges):
	result = []
	for r in ranges:
		number = 0
		for birthday in birthdays:
			if (birthday in range(r[0], r[1] + 1)):
				number += 1
		result.append(number)
	return result


print (birthday_ranges([13,24,12,5,6], [[1,3], [2,15]]))
