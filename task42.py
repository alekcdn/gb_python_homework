# 2. Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

n = int(input('Введите натуральное число : '))


def int_fact(n):
    i = 2
    mult_lst = []
    while i * i <= n:
        while n % i == 0:
            mult_lst.append(i)
            n = n / i
        i += 1
    if n > 1:
        mult_lst.append(n)
    return mult_lst


print(f'Список простых множителей числа {n} => {int_fact(n)}')
