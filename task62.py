# 2 – Дана последовательность чисел. Получить список уникальных
# элементов заданной последовательности, список повторяемых
# и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from random import randint, random
lst = [randint(-10, 10) for i in range(20)]
# lst = [1, 2, 3, 5, 1, 5, 3, 10]
non_rep_lst = []
rep_lst = []

for i in lst:
    if lst.count(i) == 1:
        non_rep_lst.append(i)
    else:
        if i not in rep_lst:
            rep_lst.append(i)

print(f"Изначальный список : {lst}")
print(f'Неповторяющиеся элементы => {non_rep_lst}')
print(f'Повторяемые элементы => {rep_lst}')
print(f'Злементы без дубликатов => {list(set(lst))}')
