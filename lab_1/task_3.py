import random as rnd

x0 = 1  # входное значение x0
y0 = 2  # входное значение y0

r0 = 5  # радиус окружности

def CALC_PI(x0, y0, r0, ExpNmb):
    m = 0   # обнуляем количество положителяных экспериментов

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


ExpNmb = 10**4  # ДЛЯ ЗАДАНИЯ 2 ПУНКТ 1, 2, 3

print(f"Число Pi: {CALC_PI(x0, y0, r0, ExpNmb)}")   # ДЛЯ ЗАДАНИЯ 1 И ЗАДАНИЯ ДВА (ЧАСТЬ 1)

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

# ЗАДАНИЕ 3 ПУНКТ 1
def CALC_EPS(SERIA):
    Eps = []

    for i in range(len(SERIA)):
        Epsi = abs((SERIA[i] - 3.1415926535) / 3.1415926535)
        Eps.append(Epsi)

    return Eps

Eps1 = CALC_EPS(SERIA_1)
Eps2 = CALC_EPS(SERIA_2)
Eps3 = CALC_EPS(SERIA_3)
Eps4 = CALC_EPS(SERIA_4)
Eps5 = CALC_EPS(SERIA_5)

# ЗАДАНИЕ 3 ПУНКТ 1 ВЫВОД
print(f"погрешность для 1й серии экспериментов: {Eps1}")
print(f"погрешность для 2й серии экспериментов: {Eps2}")
print(f"погрешность для 3й серии экспериментов: {Eps3}")
print(f"погрешность для 4й серии экспериментов: {Eps4}")
print(f"погрешность для 5й серии экспериментов: {Eps5}")


# ЗАДАНИЕ 3 ПУНКТ 2 И 3
def CALC_EPS_S_e(i):
    S_e = (SERIA_1[i] + SERIA_2[i] + SERIA_3[i] + SERIA_4[i] + SERIA_5[i]) / 5

    Eps_S_e = abs((S_e - 3.1415926535) / 3.1415926535)

    return Eps_S_e

# ЗАДАНИЕ 3 ПУНКТ 2 И 3 ВЫВОД

print(CALC_EPS_S_e(0))    # EPS_S_e4 (ExpNmb = 10**4)
print(CALC_EPS_S_e(1))    # EPS_S_e5 (ExpNmb = 10**5)
print(CALC_EPS_S_e(2))    # EPS_S_e6 (ExpNmb = 10**6)
print(CALC_EPS_S_e(3))    # EPS_S_e7 (ExpNmb = 10**7)
print(CALC_EPS_S_e(4))    # EPS_S_e8 (ExpNmb = 10**8)
