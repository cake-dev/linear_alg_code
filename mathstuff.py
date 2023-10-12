import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and an axes
fig, ax = plt.subplots()

# Initial vector
vector = np.array([1, 2])

# Scaling factor
c_values = np.linspace(1, 5, 30)

# Plot the initial vector
quiver = ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r')

# Set the axes limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Update function for animation
def update(num):
    scaled_vector = c_values[num] * vector
    quiver.set_UVC(scaled_vector[0], scaled_vector[1])

# Create an animation
ani = FuncAnimation(fig, update, frames=range(len(c_values)), blit=False)

plt.show()
