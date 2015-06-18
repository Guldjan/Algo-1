class BirthdayRanges:

    # Return a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]
    def birthdays_count(self, birthdays, ranges):
        result = []
        for r in ranges:
            number = 0
            for birthday in birthdays:
                if (birthday in range(r[0], r[1] + 1)):
                    number += 1
            result.append(number)
        return result
