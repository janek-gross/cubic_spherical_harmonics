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

<img src="https://latex.codecogs.com/gif.latex?Y_{lm}(\theta,\phi)=(-1)^m\sqrt{2}\sqrt{\frac{2l+1}{4\pi}\frac{(l-|m|)!}{(l+|m|)!}}P_l^{|m|}(cos\theta)cos(|m|\phi)" /> 
The associated legendre polynomials

<img src="https://latex.codecogs.com/gif.latex?P_l^m(x)=(-1)^{m}2^{l}(1-x^2)^{m/2}\sum_{k=m}^l\frac{k!}{(k-m)!}x^{k-m}\binom{l}{k}\binom{\frac{l+k-1}{2}}{l}" /> 
