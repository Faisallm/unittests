# test_tg_models.py
import unittest
from models.tg_models import dibenedetto, venditti_gillham, dykeman_tg
from models.kinetic_models import arrhenius, prout_thompkins, kamal_sourour, dykeman_cure
from models.elastic_modulus_model import elastic_modulus_model_A, elastic_modulus_model_B
from models.cte_model import cte_model_A, cte_model_linear
from models.cp_model import cp_model_linear
import numpy as np

class TestTGModels(unittest.TestCase):

    def setUp(self):
        self.Tg_0 = 50
        self.Tg_1 = 180
        self.lam = 0.8
        self.T_C = 150

    def test_dibenedetto_monotonic(self):
        phi = np.linspace(0.01, 0.99, 100)
        Tg_vals = dibenedetto(phi, self.Tg_0, self.Tg_1, self.lam)
        self.assertTrue(np.all(np.diff(Tg_vals) >= 0))

    def test_venditti_gillham_positive(self):
        xi = np.linspace(0.01, 0.99, 100)
        Tg_vals = venditti_gillham(xi, self.Tg_0, self.Tg_1, self.lam)
        self.assertTrue(np.all(Tg_vals > 0))

    def test_dykeman_bounds(self):
        phi = np.linspace(0.01, 0.99, 100)
        Tg_vals = [dykeman_tg(p, self.T_C, self.Tg_0, self.Tg_1, self.lam) for p in phi]
        self.assertTrue(np.all(np.array(Tg_vals) > 0))

class TestKineticModels(unittest.TestCase):

    def test_arrhenius_positive(self):
        k = arrhenius(1e5, 50, 150)
        self.assertGreater(k, 0)

    def test_prout_thompkins_bounds(self):
        phi_dot = prout_thompkins(0.5, 150, 1e5, 50, 1, 1)
        self.assertGreater(phi_dot, 0)

    def test_kamal_sourour_behavior(self):
        phi_dot = kamal_sourour(0.4, 180, 1e5, 1e3, 50, 40, 1, 2)
        self.assertGreater(phi_dot, 0)

    def test_dykeman_valid_range(self):
        for phi in [0.01, 0.1, 0.9]:
            phi_dot = dykeman_cure(phi, 160, 140)
            self.assertGreaterEqual(phi_dot, 0)

    def test_dykeman_no_nan(self):
        phi_dot = dykeman_cure(0.05, 160, 140)
        self.assertFalse(np.isnan(phi_dot))


class TestElasticModulusModels(unittest.TestCase):

    def test_model_A_above_gel(self):
        phi = 0.5
        T = 100
        E = elastic_modulus_model_A(phi, T, 0.4, 180, 0.2, 0.1, 0.05, 0.02, 1000, 0.1, 10, 1)
        self.assertGreater(E, 0.0)

    def test_model_B_above_gel(self):
        phi = 0.6
        T = 120
        phi_MD = np.linspace(0.4, 1.0, 10)
        E_MD = np.linspace(0.1, 2.0, 10)
        E = elastic_modulus_model_B(phi, T, 0.4, 200, 200, 1.2, 0.6, 0.3, 0.05, 0.1, 0.5, 0.1, 2.0, 3.0, phi_MD, E_MD)
        self.assertGreater(E, 0.0)

class TestCteModels(unittest.TestCase):

    def test_cte_A_behavior(self):
        phi = np.linspace(0, 1, 100)
        gel = 0.45
        alpha, beta = 80, 70
        cte_vals = cte_model_A(phi, gel, alpha, beta)
        self.assertTrue(np.all(cte_vals > 0))

    def test_cte_linear_behavior(self):
        phi = np.linspace(0, 1, 100)
        alpha, beta = 90, 10
        cte_vals = cte_model_linear(phi, alpha, beta)
        self.assertTrue(np.all(cte_vals > 0))

class TestCpModel(unittest.TestCase):

    def test_cp_positive(self):
        T = np.linspace(20, 500, 100)
        cp_vals = cp_model_linear(T, 1.2e-3, 0.2)
        self.assertTrue(np.all(cp_vals > 0))

    def test_cp_increasing(self):
        T = np.linspace(0, 1000, 200)
        cp_vals = cp_model_linear(T, 1.5e-3, 0.1)
        self.assertTrue(np.all(np.diff(cp_vals) >= 0))

if __name__ == '__main__':
    unittest.main()


