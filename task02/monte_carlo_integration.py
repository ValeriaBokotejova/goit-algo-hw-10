import numpy as np
import matplotlib.pyplot as plt

# Function to integrate
def f(x):
    return x**2

# Integration limits
a = 0
b = 2

# Monte Carlo method
N = 10000  # Number of random points
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Area under the curve
under_curve = y_random < f(x_random)
area = (b - a) * f(b) * np.mean(under_curve)

print(f"Monte Carlo integration estimate: {area}")

# Plotting the function and the area under the curve
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration graph of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()