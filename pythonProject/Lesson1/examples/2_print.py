# Функція print може приймати кілька параметрів
# коли ми передаємо кілька значень у функцію, то вони
# розділяються комами

# c=[ c  for c in 'llii' if c!='i']
# print(c)
#
# c=[ c*3  for c in range(7)]
# print(c)
#
# lst=[c*3 for c in range(3) if (c%3)!=0]
# print(lst)
#
# lst=[[" "],1,0," "]
# print(lst)
# print (lst.count(" "))
#
# lst =['1','2']
# lst.extend(list('34'))
# print(lst)

# Наш список `x`
from typing import List

x = [1,2,3,4,5,6,7,8,9]
# Разбиваем `x` на 3 части
y = zip(*[iter(x)]*3)
# Выводим результат
print(list(y))

# Данная функция разбивает список на равные части
def chunks(list, chunkSize):
    """Yield successive chunkSize-sized chunks from list."""
    for i in range(0, len(list), chunkSize):
        yield list[i:i + chunkSize]
# Выводим результаты на экран
import pprint
pprint.pprint(list(chunks(range(10, 90), 10)))