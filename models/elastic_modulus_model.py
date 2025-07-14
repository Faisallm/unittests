import numpy as np

def elastic_modulus_model_A(phi, temperature, gel_point, temp_ref, eta_0_A, eta_0_B, deta_0_A, deta_0_B, A1_A, A1_B, A2_A, A2_B):
    if phi < gel_point:
        return 1e-6
    temp_star = min(temperature, temp_ref)
    eta = 1.0 - (temp_star + 273.15)/(temp_ref + 273.15)
    eta_0 = eta_0_A * phi + eta_0_B
    deta = deta_0_A * phi + deta_0_B
    A1 = A1_A * np.exp(A1_B * phi)
    A2 = A2_A * phi + A2_B
    return A2 + (A1 - A2)/(1 + np.exp((eta - eta_0)/deta))

def linear_interpolation_from_lookup(phi, phi_arr, E_arr):
    return np.interp(phi, phi_arr, E_arr)

def elastic_modulus_model_B(phi, temperature, gel_point, temp_max, high_ref_temp, eta_1_A, eta_1_B, eta_0_A, eta_0_B, deta, phi_0, dphi, A_1, A_2, phi_MD, E_MD):
    if phi < gel_point:
        return 1e-6
    temp_eff = min(temperature, temp_max)
    eta = 1 - (temp_eff + 273.15)/(high_ref_temp + 273.15)
    eta_1 = eta_1_A * (eta ** eta_1_B)
    eta_0 = eta_0_A * phi + eta_0_B
    f_eta = (1 - (1 + np.exp(1 + ((eta - eta_0)/deta)))**(-1)) * eta_1
    f_phi = 1 - (1 + np.exp(1 + ((phi - phi_0)/dphi)))**(-1)
    f_A = A_1 * np.log(0.001/2.0e8) + A_2
    E_interp = linear_interpolation_from_lookup(phi, phi_MD, E_MD)
    return E_interp * f_A * f_phi * f_eta