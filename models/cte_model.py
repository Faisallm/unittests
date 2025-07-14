def cte_model_A(phi, gelation, alpha, beta):
    """CTE model A as a function of cure state."""
    return (alpha - beta*(phi - gelation))*1e-5

def cte_model_linear(phi, alpha, beta):
    """Linear CTE model as a function of cure state."""
    return (alpha * phi + beta)*1e-5