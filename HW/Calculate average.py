A = [1, 8, 3, -1, 4, 12, 7]
def avg(A):
  S = 0
  for i in A:
    S += i
  S = S / len(A)
  return S
Sred = avg(A)
print(Sred)

# Нормальное решение) 
# я его записал чуть покорче

def avg(A):
    return sum(A) / len(A)
