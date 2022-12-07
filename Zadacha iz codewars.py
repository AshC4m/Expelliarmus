# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad

lsst=[55,12,3,5,7,2,]
def invert(lsst):
    return [ n * -1 for n in lsst ] if len(lsst) > 0 else []
print(invert(lsst))

