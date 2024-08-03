# Monte Carlo Integration vs Analytical Integration

## Introduction
This project compares the Monte Carlo method and analytical integration using the function \(f(x) = x^2\) over the interval [0, 2]. The goal is to estimate the integral using Monte Carlo simulation and compare it with the exact value obtained through the `quad` function from the SciPy library.

## Files Description
- **monte_carlo_integration.py**: Implements the Monte Carlo method to estimate the integral.
- **analytical_integration.py**: Calculates the exact value of the integral using the SciPy library.

## Results
- **Monte Carlo Estimate**: The Monte Carlo method provided an estimate of the integral by averaging the proportion of random points that fall under the curve of the function.
- **Analytical Result**: The exact value of the integral calculated using the `quad` function.

## Conclusion
The Monte Carlo method gives a reasonable approximation of the integral, but the exact value calculated analytically is more precise. The difference between the two results depends on the number of random points used in the Monte Carlo simulation. Increasing the number of points improves the accuracy of the Monte Carlo estimate.
