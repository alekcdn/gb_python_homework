# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k : '))

k_lst = [randint(0, 100) for i in range(k)]+[randint(0, 100)]

res = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(k_lst) if j][::-1])
res = res.replace('x^1+', 'x+')
res = res.replace('x^0', '')
res += ('', '1')[res[-1] == '+']
res = (res, res[:-2])[res[-2:] == '^1']
res += (' = 0')

print(f'к = {k} -> {res}')

f = open('gb_python_homework/data.txt','a')
f.write(f'{res}\n')
f.close()