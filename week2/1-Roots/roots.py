class Roots:

    def square_root(self, number):
        if number < 0:
            return ValueError

        low = 0
        high = number

        while low < high:
            mid = low + (high - low) / 2
            square = mid * mid
            if abs(square - number) < 0.000001:
                return mid
            elif square > number:
                high = mid
            else:
                low = mid
