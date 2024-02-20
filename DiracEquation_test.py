import numpy as np
import matplotlib.pyplot as plt

# Parameters
x = np.linspace(0, 10, 1000)  # Position from 0 to 10
wavefunction = np.sin(x) ** 2  # Square of sine wave to represent probability density

# Plotting the probability density
plt.figure(figsize=(10, 4))
plt.plot(x, wavefunction, label='Probability Density')

# Annotating spin with arrows
for position in np.linspace(1, 9, 9):
    plt.annotate('', xy=(position, 0.5), xytext=(position, 0),
                 arrowprops=dict(facecolor='red' if position % 2 == 0 else 'blue', shrink=0.05))

plt.title('Simplified Visualization of a Quantum Particle (Red and Blue Arrows Indicate Spin)')
plt.xlabel('Position')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
