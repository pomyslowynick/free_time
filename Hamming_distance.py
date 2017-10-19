
def hammingDistance(x, y):
    dist = 0
    val = x ^ y

    while val != 0:
        dist += 1
        print(val)
        val &= val - 1
        print("After: " + str(val))
    return dist


print(hammingDistance(245673, 7890))
