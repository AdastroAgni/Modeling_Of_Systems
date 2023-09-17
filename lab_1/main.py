import random as rnd
#
# x0 = 1 #входные числа x0 и y0
# y0 = 2
#
# r0 = 5 #радиус окружности
#
# # ExpNmb = int(input("Напишите нужное количество экспериментов: "))          #ДЛЯ ЗАДАНИЯ 1
#
# def CALC_PI(x0, y0, r0, ExpNmb):
#     m = 0  # обнуляем количество положителяных экспериментов
#
#     xmin = x0 - r0
#     xmax = x0 + r0
#
#     ymin = y0 - r0
#     ymax = y0 + r0
#
#     for i in range(ExpNmb):
#         p = rnd.random()
#         xp = (xmax - xmin) * p + xmin
#
#         p = rnd.random()
#         yp = (ymax - ymin) * p + ymin
#
#         if (xp - x0) ** 2 + (yp - y0) ** 2 < r0 ** 2:
#             m += 1
#
#     pi = (m / ExpNmb) * 4
#     return pi
#
#
# ExpNmb = 10**4 # ДЛЯ ЗАДАНИЯ 2 ПУНКТ 1, 2, 3
#
#
# # print(f" число пи: {CALC_PI(x0, y0, r0, ExpNmb)}")  # ДЛЯ ЗАДАНИЯ 1 И ЗАДАНИЯ ДВА (ЧАСТЬ 1)
#
#
# # ДЛЯ ЗАДАНИЯ 2 ПУНКТ 2 И ПУНКТ 3
#
# def SERIA(ExpNmb):
#     SERIA_test = []
#
#     for i in range(5):
#         SERIA_test.append(CALC_PI(x0, y0, r0, ExpNmb))
#         ExpNmb = ExpNmb * 10
#
#     return SERIA_test
#
#
# # ДЛЯ ЗАДАНИЯ 2 ПУНКТ 2 И 3
#
# SERIA_1 = SERIA(ExpNmb)
# SERIA_2 = SERIA(ExpNmb)
# SERIA_3 = SERIA(ExpNmb)
# SERIA_4 = SERIA(ExpNmb)
# SERIA_5 = SERIA(ExpNmb)
#
# # ДЛЯ ЗАДАНИЯ 2 ПУНКТ 2 И 3 вывод
#
# # print(f"SERIA_1: {SERIA_1}")
# # print(f"SERIA_2: {SERIA_2}")
# # print(f"SERIA_3: {SERIA_3}")
# # print(f"SERIA_4: {SERIA_4}")
# # print(f"SERIA_5: {SERIA_5}")
#
# # ЗАДАНИЕ 3 ПУНКТ 1
#
# def CALC_EPS(SERIA):
#     Eps = []
#
#     for i in range(len(SERIA)):
#         Epsi = abs((SERIA[i] - 3.1415926535) / 3.1415926535)
#         Eps.append(Epsi)
#
#     return Eps
#
# Eps1 = CALC_EPS(SERIA_1)
# Eps2 = CALC_EPS(SERIA_2)
# Eps3 = CALC_EPS(SERIA_3)
# Eps4 = CALC_EPS(SERIA_4)
# Eps5 = CALC_EPS(SERIA_5)
#
# # ЗАДАНИЕ 3 ПУНКТ 1 ВЫВОД
#
# # print(f"погрешность для 1й серии экспериментов: {Eps1}")
# # print(f"погрешность для 2й серии экспериментов: {Eps2}")
# # print(f"погрешность для 3й серии экспериментов: {Eps3}")
# # print(f"погрешность для 4й серии экспериментов: {Eps4}")
# # print(f"погрешность для 5й серии экспериментов: {Eps5}")
#
#
# # ЗАДАНИЕ 3 ПУНКТ 2 И 3
#
# def CALC_EPS_S_e(i):
#     S_e = (SERIA_1[i] + SERIA_2[i] + SERIA_3[i] + SERIA_4[i] + SERIA_5[i]) / 5
#
#     Eps_S_e = abs((S_e - 3.1415926535) / 3.1415926535)
#
#     return Eps_S_e
#
# # ЗАДАНИЕ 3 ПУНКТ 2 И 3 ВЫВОД
#
# print(CALC_EPS_S_e(0))    # EPS_S_e4 (ExpNmb = 10**4)
# print(CALC_EPS_S_e(1))    # EPS_S_e5 (ExpNmb = 10**5)
# print(CALC_EPS_S_e(2))    # EPS_S_e6 (ExpNmb = 10**6)
# print(CALC_EPS_S_e(3))    # EPS_S_e7 (ExpNmb = 10**7)
# print(CALC_EPS_S_e(4))    # EPS_S_e8 (ExpNmb = 10**8)


# ЗАДАНИЕ 4 ПУНКТ 2 (ПУНКТ 1 ЯВЛЯЕТСЯ ТЕОРИЕЙ)

a = 0
b = 2

f_b = b ** 3 + 1

ExpNmb_ = 10**4


def CALC_INTEGRAL(a, b, f_b, ExpNmb_):
    x_min = a  # a = x_min
    x_max = b  # b = x_max

    y_min = 0
    y_max = f_b

    m_ = 0

    for i in range(ExpNmb_):
        p = rnd.random()

        x = (x_max - x_min) * p + x_min

        p = rnd.random()

        y = (y_max - y_min) * p + y_min

        if (x ** 3 + 1) > y:
            m_ += 1

    S = (m_ / ExpNmb_) * (b - a) * f_b
    return S


print(f" Интеграл: {CALC_INTEGRAL(a, b, f_b, ExpNmb_)}")


# ЗАДАНИЕ 4 ПУНКТ 3 (СОЗДАНИЕ ПЯТИ ВЕКТОРОВ VEK_INT)  (КАК В ЗАДАНИИ 2)

def VEK_INT(ExpNmb_):
    VEK_INT_test = []

    for i in range(5):
        VEK_INT_test.append(CALC_INTEGRAL(a, b, f_b, ExpNmb_))
        ExpNmb_ = ExpNmb_ * 10

    return VEK_INT_test


VEK_INT_1 = VEK_INT(ExpNmb_)
VEK_INT_2 = VEK_INT(ExpNmb_)
VEK_INT_3 = VEK_INT(ExpNmb_)
VEK_INT_4 = VEK_INT(ExpNmb_)
VEK_INT_5 = VEK_INT(ExpNmb_)

# print(f"VEK_INT_1: {VEK_INT_1}")
# print(f"VEK_INT_2: {VEK_INT_2}")
# print(f"VEK_INT_3: {VEK_INT_3}")
# print(f"VEK_INT_4: {VEK_INT_4}")
# print(f"VEK_INT_5: {VEK_INT_5}")


# РАСЧЕТ ПОГРЕШНОСТИ (КАК В ЗАДАНИИ 3 ПУНКТ 1)

def CALC_EPS_VEK(VEK_INT):
    Eps_VEK = []

    for i in range(len(VEK_INT)):
        Eps_VEKi = abs((VEK_INT[i] - 6) / 6)
        Eps_VEK.append(Eps_VEKi)

    return Eps_VEK

Eps_VEK_1 = CALC_EPS_VEK(VEK_INT_1)
Eps_VEK_2 = CALC_EPS_VEK(VEK_INT_2)
Eps_VEK_3 = CALC_EPS_VEK(VEK_INT_3)
Eps_VEK_4 = CALC_EPS_VEK(VEK_INT_4)
Eps_VEK_5 = CALC_EPS_VEK(VEK_INT_5)

# print(f"погрешность для 1й серии экспериментов: {Eps_VEK_1}")
# print(f"погрешность для 2й серии экспериментов: {Eps_VEK_2}")
# print(f"погрешность для 3й серии экспериментов: {Eps_VEK_3}")
# print(f"погрешность для 4й серии экспериментов: {Eps_VEK_4}")
# print(f"погрешность для 5й серии экспериментов: {Eps_VEK_5}")

# РАСЧЕТ ПОГРЕШНОСТИ (КАК В ЗАДАНИИ 3 ПУНКТ 2 и 3)

def CALC_EPS_S_e_VEK(i):
    S_e_VEK = (VEK_INT_1[i] + VEK_INT_2[i] + VEK_INT_3[i] + VEK_INT_4[i] + VEK_INT_5[i]) / 5

    Eps_S_e_VEK = abs((S_e_VEK - 6) / 6)

    return Eps_S_e_VEK

print(CALC_EPS_S_e_VEK(0))    # EPS_S_e4 (ExpNmb = 10**4)
print(CALC_EPS_S_e_VEK(1))    # EPS_S_e5 (ExpNmb = 10**5)
print(CALC_EPS_S_e_VEK(2))    # EPS_S_e6 (ExpNmb = 10**6)
print(CALC_EPS_S_e_VEK(3))    # EPS_S_e7 (ExpNmb = 10**7)
print(CALC_EPS_S_e_VEK(4))    # EPS_S_e8 (ExpNmb = 10**8)

