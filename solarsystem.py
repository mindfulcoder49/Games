import pygame
import math
import sys
from pygame.locals import *

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

# Screen setup for fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption('2D Solar System Simulation')
clock = pygame.time.Clock()

# Fonts
font_title = pygame.font.Font(None, 74)
font_instructions = pygame.font.Font(None, 36)

# Function to display the welcome screen
def welcome_screen():
    title_text = font_title.render('2D Solar System', True, WHITE)
    instructions_text = font_instructions.render('Press SPACE to Start', True, WHITE)

    while True:
        screen.fill(BLACK)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return  # Exit the welcome screen to start the simulation

        pygame.display.flip()
        clock.tick(60)

# Define celestial bodies
sun = {'color': YELLOW, 'radius': 50}
bodies = [
    {'name': 'Mercury', 'color': DARK_GRAY, 'radius': 5, 'orbit_radius_x': 100, 'orbit_radius_y': 90, 'angle': 0, 'speed': 0.03},
    {'name': 'Venus', 'color': ORANGE, 'radius': 8, 'orbit_radius_x': 150, 'orbit_radius_y': 130, 'angle': 0, 'speed': 0.02},
    {'name': 'Earth', 'color': BLUE, 'radius': 10, 'orbit_radius_x': 200, 'orbit_radius_y': 150, 'angle': 0, 'speed': 0.01},
    {'name': 'Mars', 'color': RED, 'radius': 7, 'orbit_radius_x': 250, 'orbit_radius_y': 200, 'angle': 0, 'speed': 0.008},
    {'name': 'Jupiter', 'color': LIGHT_BLUE, 'radius': 20, 'orbit_radius_x': 350, 'orbit_radius_y': 300, 'angle': 0, 'speed': 0.005},
    {'name': 'Saturn', 'color': LIGHT_GREEN, 'radius': 18, 'orbit_radius_x': 450, 'orbit_radius_y': 350, 'angle': 0, 'speed': 0.004},
    {'name': 'Uranus', 'color': GRAY, 'radius': 15, 'orbit_radius_x': 550, 'orbit_radius_y': 500, 'angle': 0, 'speed': 0.003},
    {'name': 'Neptune', 'color': DARK_GRAY, 'radius': 14, 'orbit_radius_x': 650, 'orbit_radius_y': 550, 'angle': 0, 'speed': 0.002},
]

# Define moons around each planet
moons = [
    {'planet': 'Earth', 'color': GRAY, 'radius': 3, 'orbit_radius_x': 30, 'orbit_radius_y': 25, 'angle': 0, 'speed': 0.05},
    {'planet': 'Mars', 'color': GRAY, 'radius': 2, 'orbit_radius_x': 10, 'orbit_radius_y': 8, 'angle': 0, 'speed': 0.06},  # Phobos
    {'planet': 'Mars', 'color': GRAY, 'radius': 2, 'orbit_radius_x': 15, 'orbit_radius_y': 12, 'angle': 0, 'speed': 0.04},  # Deimos
    {'planet': 'Jupiter', 'color': WHITE, 'radius': 4, 'orbit_radius_x': 40, 'orbit_radius_y': 35, 'angle': 0, 'speed': 0.07},  # Io
    {'planet': 'Jupiter', 'color': LIGHT_BLUE, 'radius': 3, 'orbit_radius_x': 50, 'orbit_radius_y': 45, 'angle': 0, 'speed': 0.06},  # Europa
    {'planet': 'Jupiter', 'color': BROWN, 'radius': 5, 'orbit_radius_x': 60, 'orbit_radius_y': 55, 'angle': 0, 'speed': 0.05},  # Ganymede
    {'planet': 'Jupiter', 'color': DARK_GRAY, 'radius': 4, 'orbit_radius_x': 70, 'orbit_radius_y': 65, 'angle': 0, 'speed': 0.04},  # Callisto
    {'planet': 'Saturn', 'color': LIGHT_GREEN, 'radius': 5, 'orbit_radius_x': 40, 'orbit_radius_y': 35, 'angle': 0, 'speed': 0.05},  # Titan
    {'planet': 'Saturn', 'color': WHITE, 'radius': 2, 'orbit_radius_x': 30, 'orbit_radius_y': 25, 'angle': 0, 'speed': 0.06},  # Enceladus
    {'planet': 'Uranus', 'color': GRAY, 'radius': 3, 'orbit_radius_x': 35, 'orbit_radius_y': 30, 'angle': 0, 'speed': 0.05},  # Titania
    {'planet': 'Uranus', 'color': DARK_GRAY, 'radius': 3, 'orbit_radius_x': 45, 'orbit_radius_y': 40, 'angle': 0, 'speed': 0.04},  # Oberon
    {'planet': 'Neptune', 'color': WHITE, 'radius': 3, 'orbit_radius_x': 35, 'orbit_radius_y': 30, 'angle': 0, 'speed': 0.04},  # Triton
]

# Function to update and draw celestial bodies
def update_and_draw():
    screen.fill(BLACK)

    # Draw Sun in the center
    pygame.draw.circle(screen, sun['color'], (WIDTH // 2, HEIGHT // 2), sun['radius'])

    # Draw planets
    planet_positions = {}
    for body in bodies:
        body['angle'] += body['speed']
        body_x = WIDTH // 2 + body['orbit_radius_x'] * math.cos(body['angle'])
        body_y = HEIGHT // 2 + body['orbit_radius_y'] * math.sin(body['angle'])
        pygame.draw.circle(screen, body['color'], (int(body_x), int(body_y)), body['radius'])
        planet_positions[body['name']] = (body_x, body_y)

    # Draw moons
    for moon in moons:
        planet_x, planet_y = planet_positions[moon['planet']]
        moon['angle'] += moon['speed']
        moon_x = planet_x + moon['orbit_radius_x'] * math.cos(moon['angle'])
        moon_y = planet_y + moon['orbit_radius_y'] * math.sin(moon['angle'])
        pygame.draw.circle(screen, moon['color'], (int(moon_x), int(moon_y)), moon['radius'])

    pygame.display.flip()

# Main loop for the 2D solar system simulation
def main_simulation():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        update_and_draw()
        clock.tick(60)

# Start the game
welcome_screen()
main_simulation()
