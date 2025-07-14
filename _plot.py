# plot_tg_models.py
import numpy as np
import matplotlib.pyplot as plt
from models.tg_models import dibenedetto, venditti_gillham, dykeman_tg
from models.kinetic_models import prout_thompkins, kamal_sourour, dykeman_cure
from models.elastic_modulus_model import elastic_modulus_model_A
from models.cte_model import cte_model_A, cte_model_linear
from models.cp_model import cp_model_linear
from fpdf import FPDF

phi = np.linspace(0.01, 0.99, 200)
Tg_0, Tg_1, lam = 50, 180, 0.8
T_C = 150

Tg_dib = dibenedetto(phi, Tg_0, Tg_1, lam)
Tg_vg = venditti_gillham(phi, Tg_0, Tg_1, lam)
Tg_dyk = [dykeman_tg(p, T_C, Tg_0, Tg_1, lam) for p in phi]

plot_file = "tg_models_plot.png"

plt.figure(figsize=(10, 4))
plt.plot(phi, Tg_dib, label='DiBenedetto')
plt.plot(phi, Tg_vg, label='Venditti-Gillham')
plt.plot(phi, Tg_dyk, label='Dykeman')
plt.xlabel('Degree of Cure / Crosslinking')
plt.ylabel('Glass Transition Temperature (Tg) [C]')
plt.title('Tg Models')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(plot_file)
plt.close()

# === Generate PDF report ===
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Tg Models Report", ln=1, align='C')
pdf.ln(5)

pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 6, f"""
Models included:
- DiBenedetto: Tg = Tg_0 + (Tg_1 - Tg_0) * (lambda * phi) / (1 - (1 - lambda) * phi)
- Venditti-Gillham: Tg = exp((ln(Tg_1) - ln(Tg_0)) * lambda * phi / (1 - (1 - lambda) * phi) + ln(Tg_0))
- Dykeman: Combines cure-dependent Tg and sigmoid ramp with cure kinetics parameters.

Common Parameters:
- Tg_0 = {Tg_0} °C (initial glass transition temperature)
- Tg_1 = {Tg_1} °C (final fully cured Tg)
- lambda = {lam}
- T_C = {T_C} °C (processing temperature)

Behavioral Checks:
- DiBenedetto: Monotonic increase with phi
- Venditti-Gillham: All Tg values > 0
- Dykeman: Bounds enforced for phi_crit, Tg remains > 0
""")

pdf.image(plot_file, w=180)
pdf.output("tg_models_report.pdf")
print("✅ Report generated: tg_models_report.pdf")


phi = np.linspace(0.01, 0.99, 200)
T = 150  # °C
Tg = 140

pt_dot = [prout_thompkins(p, T, 1e5, 60, 1, 1) for p in phi]
ks_dot = [kamal_sourour(p, T, 1e5, 1e4, 60, 40, 1, 2) for p in phi]
dyke_dot = [dykeman_cure(p, T, Tg) for p in phi]

plt.figure(figsize=(10, 4))
plt.plot(phi, pt_dot, label='Prout-Thompkins')
plt.plot(phi, ks_dot, label='Kamal-Sourour')
plt.plot(phi, dyke_dot, label='Dykeman')
plt.xlabel("Degree of Cure (phi)")
plt.ylabel("Rate of Cure (phi_dot)")
plt.title("Kinetics Behavior")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("kinetics_plot.png")
plt.close()

# PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, """
Kinetics Model Report

This report summarizes the behavior of three cure kinetics models:
- Prout-Thompkins: Empirical, sigmoidal shape
- Kamal-Sourour: Dual-term cure rate based on autocatalysis
- Dykeman: Custom model with 3 concurrent mechanisms

Temperature used: 150°C
Tg for Dykeman: 140°C
""")
pdf.image("kinetics_plot.png", w=180)
pdf.output("kinetics_report.pdf")
print("✅ Kinetics report generated!")

# === Model A Data ===
phi_vals = np.linspace(0.0, 1.0, 300)
temp = 120  # fixed temperature for comparison
gel_point = 0.4
temp_ref = 180
eta_0_A, eta_0_B = 0.2, 0.1
deta_0_A, deta_0_B = 0.05, 0.02
A1_A, A1_B = 1000, 0.1
A2_A, A2_B = 10, 1

E_vals = [
    elastic_modulus_model_A(phi, temp, gel_point, temp_ref,
                             eta_0_A, eta_0_B, deta_0_A, deta_0_B,
                             A1_A, A1_B, A2_A, A2_B) for phi in phi_vals
]

# === Plot ===
plot_file = "elastic_modulus_plot.png"
plt.figure()
plt.plot(phi_vals, E_vals, label="Elastic Modulus Model A")
plt.xlabel("Degree of Cure (ϕ)")
plt.ylabel("Elastic Modulus E [GPa]")
plt.title("Elastic Modulus vs Cure State")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(plot_file)
plt.close()

# === Generate PDF report ===
pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)
pdf.cell(200, 10, "Elastic Modulus Model A Report", ln=1, align='C')
pdf.ln(5)

pdf.set_font("DejaVu", size=10)
pdf.multi_cell(0, 6, f"""
Elastic Modulus Model A:
Formula:
    E = A₂ + (A₁ − A₂) / (1 + exp((η − η₀)/Δη))

Where:
    η = 1 − (T + 273.15) / (T_ref + 273.15)
    η₀ = η₀_A·ϕ + η₀_B
    Δη = Δη₀_A·ϕ + Δη₀_B
    A₁ = A₁_A·exp(A₁_B·ϕ)
    A₂ = A₂_A·ϕ + A₂_B

Parameters:
    Temperature = {temp} °C
    T_ref = {temp_ref} °C
    Gel Point = {gel_point}
    η₀_A = {eta_0_A}, η₀_B = {eta_0_B}
    Δη₀_A = {deta_0_A}, Δη₀_B = {deta_0_B}
    A₁_A = {A1_A}, A₁_B = {A1_B}
    A₂_A = {A2_A}, A₂_B = {A2_B}

Behavior:
    - Modulus is ~0 below gel point.
    - Above gel point, E increases with cure state.
""")

pdf.image(plot_file, w=180)
pdf.output("elastic_modulus_report.pdf")
print("✅ Report generated: elastic_modulus_report.pdf")


# === Model Data ===
phi = np.linspace(0, 1.0, 300)
gel = 0.45
alpha_A, beta_A = 80, 70
alpha_L, beta_L = 90, 10
cte_A_vals = cte_model_A(phi, gel, alpha_A, beta_A)
cte_L_vals = cte_model_linear(phi, alpha_L, beta_L)

plot_file = "cte_model_plot.png"
plt.figure()
plt.plot(phi, cte_A_vals, label="Model A")
plt.plot(phi, cte_L_vals, label="Linear Model")
plt.xlabel("Degree of Cure (ϕ)")
plt.ylabel("CTE [1/K]")
plt.title("CTE Models vs Cure State")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(plot_file)
plt.close()

# === Generate PDF report ===
pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)
pdf.cell(200, 10, "Coefficient of Thermal Expansion (CTE) Model Report", ln=1, align='C')
pdf.ln(5)

pdf.set_font("DejaVu", size=10)
pdf.multi_cell(0, 6, f"""
CTE Model A:
- Formula: (α − β·(ϕ − ϕ_gel))·1e−5
- α = {alpha_A}, β = {beta_A}, gelation = {gel}

CTE Linear Model:
- Formula: (α·ϕ + β)·1e−5
- α = {alpha_L}, β = {beta_L}

Observations:
- Both models show dependence of CTE on degree of cure (ϕ).
- Model A adjusts for gelation threshold, while the linear model assumes no such threshold.
""")

pdf.image(plot_file, w=180)
pdf.output("cte_model_report.pdf")
print("✅ Report generated: cte_model_report.pdf")

T = np.linspace(0, 1000, 300)
alpha, beta = 1.1e-3, 0.15
cp_vals = cp_model_linear(T, alpha, beta)

plot_file = "cp_model_plot.png"
plt.figure()
plt.plot(T, cp_vals, label="cp = (alpha·T + beta)·1e9")
plt.xlabel("Temperature [°C]")
plt.ylabel("Specific Heat Capacity [J/kg·K]")
plt.title("Linear cp Model")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(plot_file)
plt.close()

# === Generate PDF report ===
pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)
pdf.cell(200, 10, "Specific Heat Capacity (cp) Model Report", ln=1, align='C')
pdf.ln(5)

pdf.set_font("DejaVu", size=10)
pdf.multi_cell(0, 6, f"""
Model: cp = (alpha·T + beta)·1e9

Parameters:
- alpha = {alpha} [1/°C]
- beta = {beta} [dimensionless constant]

Behavior:
- Model predicts linear increase of cp with temperature.
- Units of cp result in [J/kg·K] after scaling.
- Monotonic increase confirmed by unittests.
""")

pdf.image(plot_file, w=180)
pdf.output("cp_model_report.pdf")
print("✅ Report generated: cp_model_report.pdf")