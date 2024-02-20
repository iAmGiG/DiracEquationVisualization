import numpy as np
import matplotlib.pyplot as plt

# Define the position range
x = np.linspace(0, 10, 100)

# Simple wave function for demonstration
wavefunction = np.cos(x)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x, wavefunction, label='Wave Function')

# Adding arrows to symbolize spin
for position in np.arange(1, 10, 2):
    plt.annotate('', xy=(position, 0.5), xytext=(position, -0.5),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    plt.annotate('', xy=(position + 1, -0.5), xytext=(position + 1, 0.5),
                 arrowprops=dict(facecolor='blue', shrink=0.05))

plt.title('Symbolic Representation of Spin')
plt.xlabel('Position')
plt.ylabel('Wave Function')
plt.legend()
plt.grid(True)
plt.show()
