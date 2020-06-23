# cubic_spherical_harmonics
The cubic spherical harmonic functions form an orthogonal basis of the 3-dimensional space.

# Requirements
- [x] sympy
- [x] numpy
- [x] scipy

## Spherical Bessel Functions
The spherical bessel functions constitute the radial part of the wave function.
Accordung to Rayleigh's<sup>1</sup> formulas the spherical bessel functions can be computed by recursion:

<img src="https://latex.codecogs.com/gif.latex?j_n(z)=(-\frac{1}{z}\frac{d}{dz})^n\frac{sin(z)}{z}" /> 

The file spherical_bessel_functions.txt contains the formulas for the first 100 spherical bessel functions. 

<sup>1</sup>http://people.math.sfu.ca/~cbm/aands/page_439.htm
