import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_aspect('equal')  # Set the aspect ratio to 1:1

ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-1.2, 1.2)
ax2.set_aspect('equal')  # Set the aspect ratio to 1:1

# Initialize empty plots for the point p(t) and the curve in each subplot
point1, = ax1.plot([], [], 'ro')
curve1, = ax1.plot([], [], 'k-')

point2, = ax2.plot([], [], 'ro')
curve2, = ax2.plot([], [], 'k-')

# Function to initialize the plots
def init():
    point1.set_data([], [])
    curve1.set_data([], [])
    point2.set_data([], [])
    curve2.set_data([], [])
    return point1, curve1, point2, curve2

# Function to update the plots in each animation frame
def update(frame):
    t = frame * 0.01 * (2 * np.pi)  # Adjust the speed of animation here
    
    # Update the first subplot
    x1 = np.sin(t)
    y1 = np.sin(t) * np.cos(t)
    point1.set_data(x1, y1)
    
    t_values1 = np.linspace(0, t, 1000)
    x_curve1 = np.sin(t_values1)
    y_curve1 = np.sin(t_values1) * np.cos(t_values1)
    curve1.set_data(x_curve1, y_curve1)
    
    # Update the second subplot
    x2 = np.sin(2*t)
    y2 = np.sin(2*t) * np.cos(2*t)
    point2.set_data(x2, y2)
    
    t_values2 = np.linspace(0, t, 1000)
    x_curve2 = np.sin(2 * t_values2)
    y_curve2 = np.sin(2 * t_values2) * np.cos(2 * t_values2)
    curve2.set_data(x_curve2, y_curve2)
    
    return point1, curve1, point2, curve2

# Create the animations
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True)


# Save the animations as GIFs
ani.save('lemniscate_animated.gif', writer='pillow', fps=30)

# Show the animations
plt.show()
