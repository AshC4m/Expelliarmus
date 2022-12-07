# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = [
    ['Waste a Moment',3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# duration = [3.03 , 4.02, 3.40, 3.03, 5.28, 4.15, 4.04, 2.58, 4.02]
# sum == 0
# for i in 3:
#     nam = input ('Название' +str(i+1)+'песни:')
#     timer = my_favorite_songs [nam]
#     sum = sum + timer
# print('сумма времени проигрывания песен =', sum, 'минут')
#
# print ()

tri_pesni = my_favorite_songs[2][1] +my_favorite_songs[5][1]+my_favorite_songs[8][1]
tri_pesni = round (tri_pesni, 2)
print ('Три песни звучат', tri_pesni, 'минут')