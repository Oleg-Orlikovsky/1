a = int(input('Введите число a:'))
amax = 0
i = a
while i:
    if i % 10 > amax:
        amax = i % 10
    i //= 10
print('Максимальная цифра числа', a, ':', amax)
