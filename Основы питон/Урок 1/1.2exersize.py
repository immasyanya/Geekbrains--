sec = int(input('Введите время в секудах: '))

hour = sec // 3600
minute = sec // 60 - hour * 60
sec_1 = sec % 60

print(f"{hour:02}.{minute:02}.{sec_1:02}")