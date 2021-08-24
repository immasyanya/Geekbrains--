n = int(input('Введите положительное число: '))
n_max = 0
i = n

while i > 1:
    i = n % 10
    if i > n_max:
        n_max = i
        if n_max == 9:
            break
    n = n // 10

print(f'Максимальная цифра в введенном числе {n_max}')