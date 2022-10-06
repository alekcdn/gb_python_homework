# 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной
# последовательности.
# lst = list(map(int, input("Введите числа через пробел:\n").split()))

from random import randint
lst = [randint(-10, 10) for i in range(20)]
res_lst = []
[res_lst.append(i) for i in lst if i not in res_lst]
print(f"Изначальный список : {lst}")
print(f"Неповторяющиеся элементы : {res_lst}")
