import sympy as sym
import numpy as np

def K_l_m(l,m):
    """
    Computes the constant pre-factor for the spherical harmonic of degree l and order m
    input:
    l: int, l>=0
    m: int, -l<=m<=l
    """
    assert abs(m)<=l
    return ((2*l+1)*np.math.factorial(l-abs(m))/(4*np.pi*np.math.factorial(l+abs(m))))**0.5
    
def sin_cos_expressions(m):
    """
    Computes the necessary sympy sine and cosine expressions
    for the spherical harmonics up to and including order m.
    """
    x = sym.symbols('x')
    y = sym.symbols('y')
    
    S_m = [0]
    C_m = [1]

    for i in range(1,m+1):
        S_m += [x*S_m[i-1] + y*C_m[i-1]]
        C_m += [x*C_m[i-1] - y*S_m[i-1]]
    return S_m, C_m
    
def associated_legendre_polynomials(l,m):
    """
    Computes the sympy fomulas for the associated legendre polynomials up to and including degree l and order m.
    """
    z = sym.symbols('z')
    
    P_l_m = [[0]*(j+1) for j in range(m+1)]
    P_l_m[0][0]=1
    P_l_m[1][0]=z
    for j in range(2,l+1):
        P_l_m[j][0] = sym.simplify(((2*j-1)*z*P_l_m[j-1][0] - (j-1)*P_l_m[j-2][0])/j)
    for i in range(1,m):
        P_l_m[i][i]   = sym.simplify((1-2*i)*P_l_m[i-1][i-1])
        P_l_m[i+1][i] = sym.simplify((2*i+1)*z*P_l_m[i][i])
        for j in range(i+2,l+1):
            P_l_m[j][i] = sym.simplify(((2*j-1)*z*P_l_m[j-1][i] - (i+j-1)*P_l_m[j-2][i])/(j-i))
    
    P_l_m[m][m] = sym.simplify((1-2*m)*P_l_m[m-1][m-1])
    return P_l_m

def spherical_harmonic_functions(l, m = None):
    """
    Computes the sympy formulas for the the spherical
    harmonic functions up to including order m between degree -l and l.
    The formulas recive as arguments the x,y and z coordinate of a point on the unit sphere.
    
    input:
    l: int, l>=0
    m: int, -l<=m<=l
    """
    if m == None:
        m = l
    assert abs(m)<=l
    P_l_m = associated_legendre_polynomials(l,m)
    S_m, C_m = sin_cos_expressions(m)
    
    Y_func_l_m = [[None]*(2*j+1) for j in range(m+1)]
    for i in range(l+1):
        Y_func_l_m[i][0] = sym.simplify(K_l_m(i,0) * P_l_m[i][0])
    
    for i in range(1,l+1):
        for j in range(1,i+1):
            Y_func_l_m[i][j] = sym.simplify(2**0.5 * K_l_m(i,j) * C_m[j] * P_l_m[i][j])
    for i in range(1,l+1):
        for j in range(1,i+1):
            Y_func_l_m[i][-j] = sym.simplify(2**0.5 * K_l_m(i,-j) * S_m[j] * P_l_m[i][j])
    return Y_func_l_m
    
