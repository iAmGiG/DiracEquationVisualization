import numpy as np
import matplotlib.pyplot as plt

# Define the position range
x = np.linspace(0, 10, 1000)

# Define the wave function as a simple sinusoidal function
wavefunction = np.sin(x)**2  # Probability density is the square of the wave function

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x, wavefunction, label='Probability Density')
plt.title('Probability Density of a Quantum Particle')
plt.xlabel('Position')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
