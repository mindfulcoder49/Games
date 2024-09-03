import pygame
import numpy as np
import sounddevice as sd
import math
import sys
from pygame.locals import *
import time

# Initialize Pygame
pygame.init()

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
BROWN = (165, 42, 42)
DARK_GRAY = (169, 169, 169)
SMOOTHING_FACTOR = 0.9
LOWER_FREQ = 20
UPPER_FREQ = 20000
MIN_EXISTENCE_TIME = 100  # Minimum existence time for bodies in seconds

# Screen setup for window mode with size matching screen dimensions
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Use a window instead of fullscreen
pygame.display.set_caption('2D Solar System Simulation with Audio Interaction')
clock = pygame.time.Clock()

# Audio settings
sample_rate = 44100
block_size = 1024

# Initialize audio data
audio_data = np.zeros(block_size)

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

# Function to get audio data
def audio_callback(indata, frames, time, status):
    global audio_data
    if status:
        print(status)
    audio_data = indata[:, 0]

# Start audio stream
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate, blocksize=block_size)
stream.start()

# Function to apply exponential moving average smoothing
def smooth_data(data, prev_smooth_data, factor):
    return factor * prev_smooth_data + (1 - factor) * data

# Initialize smoothed frequency magnitudes
prev_smoothed_magnitudes = np.zeros(block_size // 2)

# Function to find the closest note
def frequency_to_note_name(frequency):
    if frequency == 0:
        return None
    note_number = 12 * np.log2(frequency / A4_FREQ)
    note_index = int(round(note_number)) % 12
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return note_names[note_index]

# Function to map frequency to screen width using logarithmic scale
def frequency_to_x_log(frequency, lower_freq, upper_freq, width):
    if frequency < lower_freq:
        frequency = lower_freq
    elif frequency > upper_freq:
        frequency = upper_freq
    log_lower = np.log10(lower_freq)
    log_upper = np.log10(upper_freq)
    log_frequency = np.log10(frequency)
    return int((log_frequency - log_lower) / (log_upper - log_lower) * width)

# Define celestial bodies
sun = {'color': YELLOW, 'radius': 50}
bodies = [
    {'name': 'Earth', 'color': BLUE, 'radius': 10, 'orbit_radius_x': 200, 'orbit_radius_y': 150, 'angle': 0, 'speed': 0.01, 'moons': [], 'created_time': time.time()}
]

# Define initial moons around Earth
bodies[0]['moons'].append({'color': GRAY, 'radius': 3, 'orbit_radius_x': 30, 'orbit_radius_y': 25, 'angle': 0, 'speed': 0.05, 'tertiary_objects': [], 'created_time': time.time()})

# Function to dynamically add or remove celestial objects based on audio
def update_objects_based_on_audio(smoothed_magnitudes):
    global bodies

    current_time = time.time()
    
    # Determine number of planets based on high-magnitude frequencies
    significant_freqs = [i for i, mag in enumerate(smoothed_magnitudes) if mag > 0.2]
    
    # Adjust the number of planets dynamically
    if len(significant_freqs) > len(bodies) - 1:  # Exclude the sun
        for _ in range(len(significant_freqs) - (len(bodies) - 1)):
            # Add a new planet
            available_colors = list(note_colors.values())  # Convert to a list of colors
            new_planet = {
                'name': f'Planet {len(bodies)}',
                'color': available_colors[np.random.randint(len(available_colors))],  # Use numpy randint to select a color
                'radius': np.random.randint(20, 30),
                'orbit_radius_x': np.random.randint(100, 700),
                'orbit_radius_y': np.random.randint(80, 600),
                'angle': 0,
                'speed': np.random.uniform(0.002, 0.02),
                'moons': [],
                'created_time': current_time
            }
            bodies.append(new_planet)
    elif len(significant_freqs) < len(bodies) - 1:
        bodies = [body for body in bodies if current_time - body['created_time'] < MIN_EXISTENCE_TIME or body == bodies[0]]

    # Add moons or tertiary objects based on different frequency ranges
    for planet in bodies[1:]:
        if len(planet['moons']) < 3:  # Limit the number of moons
            if np.random.rand() > 0.95:  # Random chance to add a moon
                new_moon = {
                    'color': GRAY,
                    'radius': np.random.randint(10, 20),
                    'orbit_radius_x': np.random.randint(100, 200),
                    'orbit_radius_y': np.random.randint(80, 200),
                    'angle': 0,
                    'speed': np.random.uniform(0.03, 0.1),
                    'tertiary_objects': [],
                    'created_time': current_time
                }
                planet['moons'].append(new_moon)

        # Add tertiary objects around moons
        for moon in planet['moons']:
            if len(moon['tertiary_objects']) < 2:  # Limit tertiary objects
                if np.random.rand() > 0.98:  # Random chance to add a tertiary object
                    new_object = {
                        'color': WHITE,
                        'radius': np.random.randint(5, 10),
                        'orbit_radius_x': np.random.randint(15, 30),
                        'orbit_radius_y': np.random.randint(15, 30),
                        'angle': 0,
                        'speed': np.random.uniform(0.05, 0.2),
                        'created_time': current_time
                    }
                    moon['tertiary_objects'].append(new_object)

# Function to update and draw celestial bodies
def update_and_draw():
    screen.fill(BLACK)

    # Draw Sun in the center
    pygame.draw.circle(screen, sun['color'], (WIDTH // 2, HEIGHT // 2), sun['radius'])

    # Draw planets
    for planet in bodies:
        planet['angle'] += planet['speed']
        planet_x = WIDTH // 2 + planet['orbit_radius_x'] * math.cos(planet['angle'])
        planet_y = HEIGHT // 2 + planet['orbit_radius_y'] * math.sin(planet['angle'])
        pygame.draw.circle(screen, planet['color'], (int(planet_x), int(planet_y)), planet['radius'])

        # Draw moons
        for moon in planet['moons']:
            moon['angle'] += moon['speed']
            moon_x = planet_x + moon['orbit_radius_x'] * math.cos(moon['angle'])
            moon_y = planet_y + moon['orbit_radius_y'] * math.sin(moon['angle'])
            pygame.draw.circle(screen, moon['color'], (int(moon_x), int(moon_y)), moon['radius'])

            # Draw tertiary objects
            for obj in moon['tertiary_objects']:
                obj['angle'] += obj['speed']
                obj_x = moon_x + obj['orbit_radius_x'] * math.cos(obj['angle'])
                obj_y = moon_y + obj['orbit_radius_y'] * math.sin(obj['angle'])
                pygame.draw.circle(screen, obj['color'], (int(obj_x), int(obj_y)), obj['radius'])

    pygame.display.flip()

# Main loop for the 2D solar system simulation
def main_simulation():
    global prev_smoothed_magnitudes

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stream.stop()
                stream.close()
                pygame.quit()
                sys.exit()

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

        # Update celestial objects based on audio
        update_objects_based_on_audio(smoothed_magnitudes)

        # Update and draw all objects
        update_and_draw()
        clock.tick(60)

# Start the game
main_simulation()
