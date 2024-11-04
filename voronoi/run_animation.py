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
fig, ax = plt.subplots(figsize=(8, 6))

def update(frame):
    ax.clear()
    ca.plot(history[frame])
    ax.set_title(f'Step {frame}')

# Create a subset of frames (e.g., every 10th frame)
subset_frames = history[::10]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(len(subset_frames)), interval=100)

# Save the animation
ani.save('results/voronoi_ca_animation.mp4', writer='ffmpeg', fps=10)

plt.show()

