
def hammingDistance(x,y):
    dist = 0
    val = x ^ y

    while val != 0:
         dist += 1
         val = val >> 1
         print val
    return dist
print(hammingDistance(1,4))
