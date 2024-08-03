import scipy.integrate as spi

# Function to integrate
def f(x):
    return x**2

# Integration limits
a = 0
b = 2

# Analytical integration using quad
result, error = spi.quad(f, a, b)
print(f"Analytical integration result: {result}")