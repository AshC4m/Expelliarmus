# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python 
def solve(arr):
    D = []
    if type(arr) == str:
      S = 0
      arr = list(arr.lower())
      num = 0
      for i in arr:
          if ord(i) - 97 == num:
              S += 1
          num += 1
      D.append(S)
      return D
    for i in arr:
        i = list(i.lower())
        S = 0
        num = 0
        for j in i:
            if ord(j) - 97 == num:
                S += 1
            num += 1
        D.append(S)
    return D
print(solve(['abcd','abcdeeeeeee']))
