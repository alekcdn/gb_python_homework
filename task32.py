# 2. Напишите программу, которая найдёт произведение пар чисел
# списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input('Введите число элементов списка N : '))
lst = []
lst_res = []

for i in range(n):
    lst.append(randint(-n, n))

for i in range((len(lst)+1)//2):
    lst_res.append(lst[i]*lst[len(lst)-1-i])
print(f'{lst} => {lst_res}')
