# https://www.codewars.com/kata/525e5a1cb735154b320002c8
def triangular(n):
    if n <= 0:
        return 0
    s = 0
    i = 1
    while i <= n:
        s += i
        i += 1
    return s
