import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from modules.ca import VoronoiCA

n_cells = 1000
mu = 0.0
sigma = 0.42
steps = 1000

# Run
initial_state = np.random.randint(0, 2, n_cells)

ca = VoronoiCA(n_cells, mu=mu, sigma=sigma)
history = ca.evolve(initial_state, steps=steps)

# Set up the figure
fig, ax = plt.subplots()

def update(frame):
    ax.clear()  # Clear the axes
    ca.plot(history[frame])  # Plot the current state
    ax.set_title(f'Step {frame}')  # Optional: Title for each frame

# Create the animation
ani = FuncAnimation(fig, update, frames=range(len(history)), interval=100)

# Save the animation
ani.save('results/voronoi_ca_animation.mp4', writer='ffmpeg', fps=10)

plt.show()  # Show the final figure (optional)
