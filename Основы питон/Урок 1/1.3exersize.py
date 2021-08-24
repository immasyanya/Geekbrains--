n = input('Введите число: ')

while n < '0':
    print('Число меньше нуля, введите положительное число')
    n = input('Введите число: ')

print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')