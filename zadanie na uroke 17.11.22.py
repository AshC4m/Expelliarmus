# Сережа
# Создать функцию которая принимает список из отрицательных и положительных значений
# функция должна возвращать только список только из положительных значений, отрицательные должны исчезнуть
# ПОДСКАЗКА при вызове функции используй filter

lst = [1 , 3 , 4 ,5, -1, -2, -3, -4, -5, -6, 6, 7, 8, -19, 1 ,2 ]
def posneg(arr):
    return arr > 0

print (list(filter (posneg, lst) ))



  # if numbers >= 0:
  #     print ('Положительные значение:', numbers)
