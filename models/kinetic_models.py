import numpy as np

R = 0.008314  # [kJ/mol-K]

def arrhenius(A, Ea, T_C):
    T_K = T_C + 273.15
    return A * np.exp(-Ea / (R * T_K))

def prout_thompkins(phi, T_C, A, Ea, m, n):
    k = arrhenius(A, Ea, T_C)
    return k * phi**m * (1 - phi)**n

def kamal_sourour(phi, T_C, A1, A2, Ea1, Ea2, m, n):
    k1 = arrhenius(A1, Ea1, T_C)
    k2 = arrhenius(A2, Ea2, T_C)
    return (k1 + k2 * phi**m) * (1 - phi)**n

def dykeman_cure(phi, T_C, Tg):
    m1, n1 = 0, 1
    m2, n2 = 1, 2.5
    m3, n3 = 2.91, 0.83

    if T_C < 124 and phi < 0.035:
        Ac1 = 34378 * np.log(phi) + 229563
        Ac1 = max(Ac1, 50000)
        Ec1 = 73.300
    elif T_C < 124 and phi >= 0.035:
        Ac1 = 113881
        Ec1 = 73.300
    else:
        Ac1 = 14240
        Ec1 = 66.435

    Ac2, Ec2 = 473684, 73.063
    Ac3, Ec3 = 1.5e9, 115.624

    Kc1 = arrhenius(Ac1, Ec1, T_C)
    Kc2 = arrhenius(Ac2, Ec2, T_C)
    Kc3 = arrhenius(Ac3, Ec3, T_C)

    Ad12, Ed12, b12 = 4e12, 60.0, 0.5268
    Ad3, b3 = 1.5e9, 0.0147

    af, fg = 8e-5, 0.025
    fv = af * (T_C - Tg) + fg

    if T_C - Tg < -323.15:
        Kd12 = Kd3 = 1e-99
    else:
        Kd12 = arrhenius(Ad12, Ed12, T_C) + (-b12 / fv)
        Kd3 = Ad3 * np.exp(-b3 / fv)

    Ke1 = (Kc1 * Kd12) / (Kc1 + Kd12)
    Ke2 = (Kc2 * Kd12) / (Kc2 + Kd12)
    Ke3 = (Kc3 * Kd3) / (Kc3 + Kd3)

    return Ke1 * phi**m1 * (1 - phi)**n1 + Ke2 * phi**m2 * (1 - phi)**n2 + Ke3 * phi**m3 * (1 - phi)**n3
