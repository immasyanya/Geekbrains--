proceeds = float(input("Введите выручку компании: "))
costs = float(input("Введите издержки компании: "))

profit = proceeds - costs

if profit < 0:
    print(f"Вы ушли в минус! Ваша прибыль равна {profit}.")
elif profit > 0:
    profitability = proceeds / profit
    print(f"Вы вышли в плюс! Ваша прибыль равна {profit}. Ваша рентабильность равна {profitability:.1f}%.")
    worker = int(input("Введите количество сотрудников: "))
    #profit_worker = profit / worker
    print(f"Прибыль на каждого сотрудника составляет {profit / worker:.3f}")
else:
    print("Вы вышли в ноль")