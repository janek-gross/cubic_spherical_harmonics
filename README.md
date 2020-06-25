# cubic_spherical_harmonics
The cubic spherical harmonic functions form an orthogonal basis of the 3-dimensional space.

# Requirements
- [x] python 3
- [x] sympy
- [x] numpy
- [x] scipy

## Spherical Bessel Functions
The spherical bessel functions constitute the radial part of the wave function.
Accordung to Rayleigh's formula<sup>1</sup> the spherical bessel functions can be computed by recursion:

<img src="https://latex.codecogs.com/gif.latex?j_n(z)=(-\frac{1}{z}\frac{d}{dz})^n\frac{sin(z)}{z}" /> 

The file spherical_bessel_functions.txt contains the analytic formulas for the first 85 spherical bessel functions. 

<img src="https://github.com/janek-gross/cubic_spherical_harmonics/blob/master/spherical_bessel_functions.png?raw=true" width="800"  />
<sup>1</sup>http://people.math.sfu.ca/~cbm/aands/page_439.htm

## Real Spherical Harmonic Functions

The spherical haromics constitute the angular part of the wave function.
