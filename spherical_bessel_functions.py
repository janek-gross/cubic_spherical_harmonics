import sympy as sym
def spherical_bessel_function_formulas(n = 10):
    """
    Recursively computes the analytic formulas of the spherical bessl functions according to Rayleih's formula.
    -------------------------------------------------
    inputs:
    n:          A positive integer determines up which order the formulas are computed.
    
    returns:
    f:          A list of sympy formulas.
    """
    x = sym.symbols('x')
    f = [sym.sin(x)/x]
    a = sym.sin(x)/x
    for i in range(n):
        b = sym.diff(a,x)/x
        f += [sym.simplify(b*(-x)**(i+1))]
        a = sym.simplify(b)
    return f
