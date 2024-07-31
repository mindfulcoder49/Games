import pygame
import math
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Solar System Simulation')
clock = pygame.time.Clock()

# Function to project 3D points to 2D
def project_point(x, y, z, screen_width, screen_height):
    fov = 256  # Field of view
    distance = 4  # Distance from the viewer

    factor = fov / (distance + z)
    x = x * factor + screen_width / 2
    y = -y * factor + screen_height / 2
    return int(x), int(y)

# Function to rotate points in 3D space
def rotate_point(x, y, z, angle_x, angle_y, angle_z):
    # Rotate around x-axis
    cos_x = math.cos(angle_x)
    sin_x = math.sin(angle_x)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

    # Rotate around y-axis
    cos_y = math.cos(angle_y)
    sin_y = math.sin(angle_y)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

    # Rotate around z-axis
    cos_z = math.cos(angle_z)
    sin_z = math.sin(angle_z)
    x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z

    return x, y, z

# Define the planets
planets = [
    {'name': 'Sun', 'color': YELLOW, 'radius': 50, 'distance': 0, 'angle': 0, 'speed': 0},
    {'name': 'Earth', 'color': BLUE, 'radius': 10, 'distance': 200, 'angle': 0, 'speed': 0.01},
    {'name': 'Mars', 'color': RED, 'radius': 7, 'distance': 300, 'angle': 0, 'speed': 0.008}
]

# Main loop
angle_x = angle_y = angle_z = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01

    screen.fill(BLACK)

    for planet in planets:
        planet['angle'] += planet['speed']
        x = planet['distance'] * math.cos(planet['angle'])
        y = planet['distance'] * math.sin(planet['angle'])
        z = 0

        x, y, z = rotate_point(x, y, z, angle_x, angle_y, angle_z)

        x2d, y2d = project_point(x, y, z, WIDTH, HEIGHT)
        pygame.draw.circle(screen, planet['color'], (x2d, y2d), planet['radius'])

    pygame.display.flip()
    clock.tick(60)
