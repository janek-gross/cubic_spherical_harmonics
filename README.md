# cubic_spherical_harmonics
The cubic spherical harmonic functions form an orthogonal basis of the 3-dimensional space. These functions are the fourier basis of the 3 dimensional space in spherical coordinates with radius <img src="https://latex.codecogs.com/gif.latex?r" /> longitude <img src="https://latex.codecogs.com/gif.latex?\theta" /> and latitude <img src="https://latex.codecogs.com/gif.latex?\phi" />.
Each of these so called wave functions consists of radial part and an angular part.
This repository contains the formulas of the real parts of these wave functions.
<img src="https://latex.codecogs.com/gif.latex?\psi_{nlm}(r,\theta,\phi)=j_n(r)Y_{lm}(\theta,\phi)" /> 
<img src="https://github.com/janek-gross/cubic_spherical_harmonics/blob/master/wave_functions.gif?raw=true" width="800"  />

# Requirements
- [x] python 3
- [x] sympy
- [x] numpy
- [x] scipy

## Spherical Bessel Functions
The spherical bessel functions constitute the radial part of the wave function.
Accordung to Rayleigh's formula<sup>1</sup> the spherical bessel functions can be computed by recursion:

<img src="https://latex.codecogs.com/gif.latex?j_n(r)=(-\frac{1}{r}\frac{d}{dr})^n\frac{sin(r)}{r}" /> 

The file spherical_bessel_functions.txt contains the analytic formulas for the first 85 spherical bessel functions. 

<img src="https://github.com/janek-gross/cubic_spherical_harmonics/blob/master/spherical_bessel_functions/spherical_bessel_functions.png?raw=true" width="800"  />
<sup>1</sup>http://people.math.sfu.ca/~cbm/aands/page_439.htm

## Real Spherical Harmonic Functions

The spherical haromics constitute the angular part of the wave function.

<img src="https://latex.codecogs.com/gif.latex?Y_{lm}(\theta,\phi)=\begin{cases}{\displaystyle}(-1)^m\sqrt{2}\sqrt{\frac{2l+1}{4\pi}\frac{(l-|m|)!}{(l+|m|)!}}P_l^{|m|}(cos\theta)sin(|m|\phi)\\{\displaystyle}(-1)^m\sqrt{\frac{2l+1}{4\pi}}P_l^{m}(cos\theta)\\{\displaystyle}(-1)^m\sqrt{2}\sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}P_l^{m}(cos\theta)cos(m\phi)\end{cases}" /> 

Where <img src="https://latex.codecogs.com/gif.latex?P_l^m" /> are the associated legendre polynomials

<img src="https://latex.codecogs.com/gif.latex?P_l^m(x)=(-1)^{m}2^{l}(1-x^2)^{m/2}\sum_{k=m}^l\frac{k!}{(k-m)!}x^{k-m}\binom{l}{k}\binom{\frac{l+k-1}{2}}{l}" /> 





