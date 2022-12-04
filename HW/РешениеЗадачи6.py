# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
songs = []
for i in my_favorite_songs:
  songs.append(my_favorite_songs[i])
time = 0
i = 0
while i < 3:
  import random
  k = random.randint(0,len(songs) - 1)
  time += songs[k]
  songs.remove(songs[k])
  i += 1
print(f"Три песни звучат {time} минут")
