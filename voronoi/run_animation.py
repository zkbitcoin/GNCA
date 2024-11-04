import os
import matplotlib.pyplot as plt
import numpy as np
from modules.ca import VoronoiCA
import subprocess

n_cells = 1000
mu = 0.0
sigma = 0.42
steps = 1000

# Run
initial_state = np.random.randint(0, 2, n_cells)

ca = VoronoiCA(n_cells, mu=mu, sigma=sigma)
history = ca.evolve(initial_state, steps=steps)

# Create a directory to store frames
if not os.path.exists('frames'):
    os.makedirs('frames')

# Capture frames
for i, state in enumerate(history):
    plt.figure(figsize=(8, 6))
    ca.plot(state)
    plt.title(f'Step {i}')
    plt.axis('off')  # Turn off axis
    plt.savefig(f'frames/frame_{i:04d}.png')  # Save each frame as an image
    plt.close()  # Close the figure to save memory
    print(f"Saved frame {i}")  # Optional: Print progress

# Create a video from frames using FFmpeg
ffmpeg_command = [
    'ffmpeg',
    '-framerate', '10',  # Adjust frame rate as needed
    '-i', 'frames/frame_%04d.png',  # Input pattern
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    'results/voronoi_ca_animation.mpg'  # Output file
]

# Run the command and capture output
process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print FFmpeg output for debugging
print(process.stdout.decode())
print(process.stderr.decode())

# Clean up frames (optional)
import shutil
shutil.rmtree('frames')

