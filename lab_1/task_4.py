import random as rnd
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

print(f"VEK_INT_1: {VEK_INT_1}")
print(f"VEK_INT_2: {VEK_INT_2}")
print(f"VEK_INT_3: {VEK_INT_3}")
print(f"VEK_INT_4: {VEK_INT_4}")
print(f"VEK_INT_5: {VEK_INT_5}")


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

print(f"погрешность для 1й серии экспериментов: {Eps_VEK_1}")
print(f"погрешность для 2й серии экспериментов: {Eps_VEK_2}")
print(f"погрешность для 3й серии экспериментов: {Eps_VEK_3}")
print(f"погрешность для 4й серии экспериментов: {Eps_VEK_4}")
print(f"погрешность для 5й серии экспериментов: {Eps_VEK_5}")

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

