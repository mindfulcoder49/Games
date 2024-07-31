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
SMOOTHING_FACTOR = 0.98
LOWER_FREQ = 50
UPPER_FREQ = 8000
THRESHOLD = 0.18
MAX_CIRCLE_SIZE = 80  # Adjust to make the biggest circles bigger

# Configurable fields
config_fields = ["SMOOTHING_FACTOR", "LOWER_FREQ", "UPPER_FREQ", "THRESHOLD", "MAX_CIRCLE_SIZE"]
config_values = [SMOOTHING_FACTOR, LOWER_FREQ, UPPER_FREQ, THRESHOLD, MAX_CIRCLE_SIZE]
current_field = 0
input_value = ""

# Note to color mapping including quarter-step notes
note_colors = {
    'C': (0, 0, 255),       # Blue
    'C quarter': (0, 63, 255),   # Light Blue
    'C#': (0, 127, 255),    # Deep Sky Blue
    'C# quarter': (0, 191, 255), # Sky Blue
    'D': (0, 255, 255),     # Cyan
    'D quarter': (0, 255, 191),  # Light Cyan
    'D#': (0, 255, 127),    # Spring Green
    'D# quarter': (0, 255, 63),  # Light Spring Green
    'E': (0, 255, 0),       # Green
    'E quarter': (63, 255, 0),   # Light Green
    'F': (127, 255, 0),     # Chartreuse
    'F quarter': (173, 255, 0),  # Light Chartreuse
    'F#': (173, 255, 47),   # Green-Yellow
    'F# quarter': (191, 255, 63), # Light Green-Yellow
    'G': (255, 255, 0),     # Yellow
    'G quarter': (255, 255, 63),  # Light Yellow
    'G#': (255, 215, 0),    # Gold
    'G# quarter': (255, 191, 63), # Light Gold
    'A': (255, 140, 0),     # Orange
    'A quarter': (255, 127, 63),  # Light Orange
    'A#': (255, 69, 0),     # Red-Orange
    'A# quarter': (255, 63, 63),  # Light Red-Orange
    'B': (255, 0, 0),       # Red
    'B quarter': (255, 63, 63)    # Light Red
}

# Frequency of A4
A4_FREQ = 440.0

# Screen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
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

# Function to find the closest note, including quarter-step notes
def frequency_to_note_name(frequency):
    if frequency == 0:
        return None
    note_number = 12 * np.log2(frequency / A4_FREQ)
    note_index = int(round(note_number * 4)) % 24
    note_names = [
        'C', 'C quarter', 'C#', 'C# quarter', 'D', 'D quarter', 'D#', 'D# quarter', 'E', 'E quarter', 'F', 'F quarter', 
        'F#', 'F# quarter', 'G', 'G quarter', 'G#', 'G# quarter', 'A', 'A quarter', 'A#', 'A# quarter', 'B', 'B quarter'
    ]
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

# Function to display the configurable fields
def display_config_fields(screen, fields, values, current_index, input_value, width, height):
    font = pygame.font.SysFont(None, 36)
    y_offset = height - 40
    for i, (field, value) in enumerate(zip(fields, values)):
        color = WHITE if i == current_index else (128, 128, 128)
        text = font.render(f"{field}: {value:.2f}", True, color)
        screen.blit(text, (10, y_offset))
        y_offset -= 40
    if input_value:
        input_text = font.render(f"Input: {input_value}", True, WHITE)
        screen.blit(input_text, (10, y_offset))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stream.stop()
            stream.close()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_field = (current_field + 1) % len(config_fields)
            elif event.key == pygame.K_LEFT:
                current_field = (current_field - 1) % len(config_fields)
            elif event.key == pygame.K_RETURN:
                if input_value:
                    try:
                        new_value = float(input_value)
                        config_values[current_field] = new_value
                    except ValueError:
                        pass
                    input_value = ""
            elif event.unicode.isdigit() or event.unicode == '.':
                input_value += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                input_value = input_value[:-1]

    # Update configurable values
    SMOOTHING_FACTOR, LOWER_FREQ, UPPER_FREQ, THRESHOLD, MAX_CIRCLE_SIZE = config_values

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
    for i, magnitude in enumerate(smoothed_magnitudes):
        if magnitude > THRESHOLD:  # Configurable threshold for circle display
            frequency = i * sample_rate / block_size
            if LOWER_FREQ <= frequency <= UPPER_FREQ:  # Only display circles within frequency range
                note_name = frequency_to_note_name(frequency)
                if note_name:
                    color = note_colors.get(note_name, WHITE)

                    # Map frequency to x coordinate using logarithmic scale
                    circle_x = frequency_to_x_log(frequency, LOWER_FREQ, UPPER_FREQ, WIDTH)
                    circle_y = HEIGHT + (magnitude/2) - int(magnitude * HEIGHT)  # Start from the bottom
                    pygame.draw.circle(screen, color, (circle_x, circle_y), int(magnitude * MAX_CIRCLE_SIZE))

    # Display configurable fields
    display_config_fields(screen, config_fields, config_values, current_field, input_value, WIDTH, HEIGHT)

    pygame.display.flip()
    clock.tick(60)
