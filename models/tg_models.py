# tg_models.py
import numpy as np

def dibenedetto(phi, Tg_0, Tg_1, lam):
    return Tg_0 + (Tg_1 - Tg_0)*(lam*phi)/(1 - (1 - lam)*phi)

def venditti_gillham(xi, Tg_0, Tg_1, lam):
    return np.exp((np.log(Tg_1) - np.log(Tg_0))*(lam*xi/(1 - (1 - lam)*xi)) + np.log(Tg_0))

def dykeman_tg(phi, T_C, Tg_0, Tg_1, lam):
    D, F, ramp = 35, 25, 2.8
    T_K = T_C + 273.15

    if ramp/60 < 0.0001:
        phi_crit = 0.0025*T_K - 0.3329
    else:
        phi_crit = 0.0025*T_K - 0.00017*60/ramp - 0.3329

    phi_crit = min(max(phi_crit, 0.675), 1.0)

    Tg = (((lam*phi*(Tg_1 - Tg_0)) / (1 - (1 - lam)*phi)) + Tg_0 + 273.15 + (D / (1 + np.exp(-F*(phi - phi_crit))))) - 273.15
    return Tg


