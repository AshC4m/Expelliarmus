# Вот ссылка на файл в google colab: https://colab.research.google.com/drive/1vvxGvU-a2yWLxA0vCMa8Zkqd-NJuWVLF?usp=sharing
# Мы открыли доступ, так что можете посмотреть. Все работает, правда только 3 раза в минуту из-за ограничений alphavantage

# Вводные данные:
cd /content/drive/MyDrive/Colab Notebooks/Project

import pandas as pd
import cred
import numpy as np '''Нужен для рассчета среднего значения'''
info = pd.read_csv('info.csv', index_col='currency') '''Импортировали info.csv и заменили индексацию на валюту для удобства'''

# Получаем данные по акциям от alphavantage
def get_data(token):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={token}&interval={time}&apikey={cred.API_KEY}&datatype=csv'
    return pd.read_csv(url)
  
# Сравниваем FastSMA и SlowSMA
def get_useful_data(df):
  fast_7 = np.mean(df['close'][0:7])
  slow_25 = np.mean(df['close'][0:25])
  if fast_7 >= slow_25:
    num = 1
  else:
    num = 0
  return num

# Конечная функция принятия решения о покупке или продаже
def trader(curr):
  df = get_data(curr)
  num = get_useful_data(df)
  if info['position'][curr] != num:
    if num == 1:
      print(f'Для {curr}. Быстрая скользящая пересекла среднюю снизу вверх, КУПИТЬ!')
    else:
      print(f'Для {curr}. Быстрая скользящая пересекла среднюю сверху вниз, ПРОДАВАТЬ!')
    info['position'][curr] = num
  elif num == 1:
    print(f'Рано продавать {curr}')
  elif num == 0:
    print(f'Рано покупать {curr}')
  return info

# Проверка
for curr in info.index:
  trader(curr)
print (info)

