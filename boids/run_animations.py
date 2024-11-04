import os
import subprocess
import shutil

# Create a video from frames using FFmpeg
ffmpeg_command = [
    'ffmpeg',
    '-framerate', '10',  # Adjust frame rate as needed
    '-i', 'frames/frame_%04d.png',  # Input pattern
    '-c:v', 'libx264',  # Use H.264 codec for compatibility
    '-pix_fmt', 'yuv420p',  # Pixel format for broader compatibility
    'results/boids_ca_animation.mp4'  # Output file
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

