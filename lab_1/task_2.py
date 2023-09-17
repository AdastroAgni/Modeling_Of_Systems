import random as rnd

x0 = 1 # входное значение x0
y0 = 2 # входное значение y0

r0 = 5 # радиус окружности

ExpNmb = 10**4 # ДЛЯ ЗАДАНИЯ 2 ПУНКТ 1, 2, 3

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


print(f"Число Pi: {CALC_PI(x0, y0, r0, ExpNmb)}")  # ДЛЯ ЗАДАНИЯ 1 И ЗАДАНИЯ ДВА (ЧАСТЬ 1)

# ДЛЯ ЗАДАНИЯ 2 ПУНКТ 2 И ПУНКТ 3
def SERIA(ExpNmb):
    SERIA_test = []

    for i in range(5):
        SERIA_test.append(CALC_PI(x0, y0, r0, ExpNmb))
        ExpNmb = ExpNmb * 10

    return SERIA_test


# ДЛЯ ЗАДАНИЯ 2 ПУНКТ 2 И 3
SERIA_1 = SERIA(ExpNmb)
SERIA_2 = SERIA(ExpNmb)
SERIA_3 = SERIA(ExpNmb)
SERIA_4 = SERIA(ExpNmb)
SERIA_5 = SERIA(ExpNmb)

# ДЛЯ ЗАДАНИЯ 2 ПУНКТ 2 И 3 вывод
print(f"SERIA_1: {SERIA_1}")
print(f"SERIA_2: {SERIA_2}")
print(f"SERIA_3: {SERIA_3}")
print(f"SERIA_4: {SERIA_4}")
print(f"SERIA_5: {SERIA_5}")
