import pygame
import numpy as np
import sounddevice as sd
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SMOOTHING_FACTOR = 0.99

# Note to color mapping
note_colors = {
    'C': (255, 0, 0),    # Red
    'C#': (255, 128, 0),  # Orange
    'D': (255, 255, 0),   # Yellow
    'D#': (128, 255, 0),  # Light Green
    'E': (0, 255, 0),     # Green
    'F': (0, 255, 128),   # Turquoise
    'F#': (0, 255, 255),  # Cyan
    'G': (0, 128, 255),   # Light Blue
    'G#': (0, 0, 255),    # Blue
    'A': (128, 0, 255),   # Purple
    'A#': (255, 0, 255),  # Magenta
    'B': (255, 0, 128)    # Pink
}

# Frequency of A4
A4_FREQ = 440.0

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Artistic Audio Visualizer')
clock = pygame.time.Clock()

# Audio settings
sample_rate = 44100
block_size = 1024

# Function to get audio data
def audio_callback(indata, frames, time, status):
    global audio_data
    if status:
        print(status)
    audio_data = indata[:, 0]

# Start audio stream
audio_data = np.zeros(block_size)
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate, blocksize=block_size)
stream.start()

# Function to apply exponential moving average smoothing
def smooth_data(data, prev_smooth_data, factor):
    return factor * prev_smooth_data + (1 - factor) * data

# Initialize smoothed frequency magnitudes
prev_smoothed_magnitudes = np.zeros(block_size // 2)

# Artificial movement variables
angle_offset = 0
angle_speed = 0.01

# Function to find the closest note
def frequency_to_note_name(frequency):
    if frequency == 0:
        return None
    note_number = 12 * np.log2(frequency / A4_FREQ)
    note_index = int(round(note_number)) % 12
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return note_names[note_index]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stream.stop()
            stream.close()
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Compute FFT and get frequency magnitudes
    fft_data = np.fft.fft(audio_data)
    freq_magnitudes = np.abs(fft_data[:len(fft_data) // 2])

    # Normalize magnitudes for visualization
    max_magnitude = np.max(freq_magnitudes)
    if max_magnitude > 0:
        freq_magnitudes /= max_magnitude

    # Smooth frequency magnitudes
    smoothed_magnitudes = smooth_data(freq_magnitudes, prev_smoothed_magnitudes, SMOOTHING_FACTOR)
    prev_smoothed_magnitudes = smoothed_magnitudes

    # Draw artistic visualization
    bar_width = WIDTH / len(smoothed_magnitudes)
    for i, magnitude in enumerate(smoothed_magnitudes):
        if magnitude > 0.1:  # Threshold to filter out noise
            frequency = i * sample_rate / block_size
            note_name = frequency_to_note_name(frequency)
            if note_name:
                color = note_colors.get(note_name, WHITE)

                # Draw rotating circles with artificial movement
                angle = math.pi * 2 * i / len(smoothed_magnitudes) + angle_offset
                circle_x = WIDTH // 2 + math.cos(angle) * (magnitude * HEIGHT * 0.5 + 100 * math.sin(angle_offset))
                circle_y = HEIGHT // 2 + math.sin(angle) * (magnitude * HEIGHT * 0.5 + 100 * math.cos(angle_offset))
                pygame.draw.circle(screen, color, (int(circle_x), int(circle_y)), int(magnitude * 50))

    # Update artificial movement
    angle_offset += angle_speed

    pygame.display.flip()
    clock.tick(60)
