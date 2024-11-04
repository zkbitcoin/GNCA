import os
import matplotlib.pyplot as plt
import numpy as np
from modules.ca import VoronoiCA
import subprocess
import shutil

n_cells = 1000
mu = 0.0
sigma = 0.42
steps = 1000

# Run the cellular automaton
initial_state = np.random.randint(0, 2, n_cells)

ca = VoronoiCA(n_cells, mu=mu, sigma=sigma)
history = ca.evolve(initial_state, steps=steps)

# Create a directory to store frames
if not os.path.exists('frames'):
    os.makedirs('frames')

# Animation and saving frames
plt.figure(figsize=(8, 6))
for i, state in enumerate(history):
    ca.plot(state)
    plt.title(f'Step {i}')
    plt.axis('off')  # Turn off axis
    plt.savefig(f'frames/frame_{i:04d}.png')  # Save each frame as an image
    plt.draw()
    plt.pause(0.1)  # Optional: pause for visual effect
    print(f"Saved frame {i}: frame_{i:04d}.png")  # Print progress

plt.close()  # Close the figure after the loop

# Create a video from frames using FFmpeg
ffmpeg_command = [
    'ffmpeg',
    '-framerate', '10',  # Adjust frame rate as needed
    '-i', 'frames/frame_%04d.png',  # Input pattern
    '-c:v', 'libx264',  # Use H.264 codec for compatibility
    '-pix_fmt', 'yuv420p',  # Pixel format for broader compatibility
    'results/voronoi_ca_animation.mp4'  # Output file
]

# Run the command and capture output
process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print FFmpeg output for debugging
print("FFmpeg STDOUT:")
print(process.stdout.decode())
print("FFmpeg STDERR:")
print(process.stderr.decode())

# Clean up frames (optional)
shutil.rmtree('frames')

