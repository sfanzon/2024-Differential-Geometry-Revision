import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure with a single subplot
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')  # Set the aspect ratio to 1:1

# Plot the static curve (deep pink with thickness 1.5)
t_values = np.linspace(-2, 2, 1000)
x_curve = t_values ** 2 - 1
y_curve = t_values ** 3 - t_values
ax.plot(x_curve, y_curve, 'deeppink', linewidth=1.5)

# Initialize the plot for the point p(t) in the subplot
point, = ax.plot([], [], 'ko', markersize=8)  # Larger point in black

# Function to initialize the plots
def init():
    point.set_data([], [])
    return point,

# Function to update the position of the point in each animation frame
def update(frame):
    speed = 0.01            # Adjusts animation speed
    initial_time = -1.5       # Adjusts initial time

    t = frame * speed + initial_time
    
    # Update the position of the point
    x = t ** 2 - 1
    y = t ** 3 - t
    point.set_data(x, y)
    
    return point,  # Note the comma at the end to return a tuple

# Create the animation
ani = FuncAnimation(fig, update, frames=350, init_func=init, blit=True)  # Adjust frames to cover the desired range

# Save the animation as a GIF
ani.save('loop_animated.gif', writer='pillow', fps=30)

# Show the animation
plt.show()

