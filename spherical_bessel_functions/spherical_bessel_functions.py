import sympy as sym
def spherical_bessel_function_formulas(n = 10):
    """
    Recursively computes the analytic formulas of the
    spherical bessel functions according to Rayleih's formula.
    The formulas receive as argument r the distance
    to the origin of a point in 3D space.
    -------------------------------------------------
    inputs:
    n:          A positive integer determines up which order the formulas are computed.
    
    returns:
    f:          A list of sympy formulas.
    """
    r = sym.symbols('r')
    f = [sym.sin(r)/r]
    a = sym.sin(r)/r
    for i in range(n):
        b = sym.diff(a,r)/r
        f += [sym.simplify(b*(-r)**(i+1))]
        a = sym.simplify(b)
    return f
