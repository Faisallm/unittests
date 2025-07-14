def cp_model_linear(temperature, alpha, beta):
    """Linear specific heat capacity model: cp = (α·T + β)·1e9"""
    return (alpha * temperature + beta) * 1e9