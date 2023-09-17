import random as rnd

x0 = 1 # входное значение x0
y0 = 2 # входное значение y0

r0 = 5 # радиус окружности

ExpNmb = int(input("Напишите нужное количество экспериментов: ")) # ДЛЯ ЗАДАНИЯ 1

def CALC_PI(x0, y0, r0, ExpNmb):
    m = 0  # обнуляем количество положителяных экспериментов

    xmin = x0 - r0
    xmax = x0 + r0

    ymin = y0 - r0
    ymax = y0 + r0

    for i in range(ExpNmb):
        p = rnd.random()
        xp = (xmax - xmin) * p + xmin

        p = rnd.random()
        yp = (ymax - ymin) * p + ymin

        if (xp - x0) ** 2 + (yp - y0) ** 2 < r0 ** 2:
            m += 1

    pi = (m / ExpNmb) * 4
    return pi

print(f"Число Pi: {CALC_PI(x0, y0, r0, ExpNmb)}")
