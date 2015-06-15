def squareroot(inputNum):
    if inputNum < 0:
        return ValueError

    low = 0
    high = inputNum

    while low < high:
        mid = low + (high - low) / 2
        square = mid * mid
        if abs(square - inputNum) < 0.000001:
            return mid
        elif square > inputNum:
            high = mid
        else:
            low = mid