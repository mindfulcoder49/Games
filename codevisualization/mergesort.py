import pygame
import sys
import time
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GREEN = (144, 238, 144)
DARK_BLUE = (25, 25, 112)
GRAY = (211, 211, 211)

FPS = 60
speed = 1  # Speed multiplier for animations

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Majestic Merge Animation")
clock = pygame.time.Clock()

# Function to draw the background gradient
def draw_background():
    for i in range(HEIGHT):
        color = (25, 25 + i // 10, 112 + i // 5)
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

# Function to draw an array
def draw_array(array, m, n, colors, positions, highlight=None):
    rect_width = WIDTH // (m + n)
    rect_height = HEIGHT // 10
    for i in range(m + n):
        color = colors[i] if i < len(colors) else WHITE
        x, y = positions[i]
        pygame.draw.rect(screen, color, [x, y, rect_width, rect_height], border_radius=10)
        font = pygame.font.Font(None, 36)
        text = font.render(str(array[i]), True, BLACK)
        screen.blit(text, (x + rect_width // 2 - 10, y + rect_height // 2 - 10))
    
    # Draw highlight (if any)
    if highlight:
        i, j = highlight
        pygame.draw.rect(screen, GRAY, [positions[i][0], positions[i][1], rect_width, rect_height], border_radius=10, width=5)
        pygame.draw.rect(screen, GRAY, [positions[j][0], positions[j][1], rect_width, rect_height], border_radius=10, width=5)

# Function to display explanations
def display_explanation(text):
    font = pygame.font.Font(None, 30)
    explanation_surface = font.render(text, True, BLACK)
    screen.blit(explanation_surface, (20, HEIGHT - 50))

# Linear interpolation function for smooth transition
def lerp(start, end, t):
    return start + t * (end - start)

# Function to animate element transition
def animate_element_transition(start_pos, end_pos, element, color, m, n, duration=1):
    start_time = time.time()
    rect_width = WIDTH // (m + n)
    rect_height = HEIGHT // 10
    while time.time() - start_time < duration / speed:
        t = (time.time() - start_time) / (duration / speed)
        x = lerp(start_pos[0], end_pos[0], t)
        y = lerp(start_pos[1], end_pos[1], t)
        
        draw_background()
        pygame.draw.rect(screen, color, [x, y, rect_width, rect_height], border_radius=10)
        font = pygame.font.Font(None, 36)
        text = font.render(str(element), True, BLACK)
        screen.blit(text, (x + rect_width // 2 - 10, y + rect_height // 2 - 10))
        pygame.display.flip()
        clock.tick(FPS)

def animate_merge(nums1, m, nums2, n):
    len1 = len(nums1)
    end_idx = len1 - 1
    colors = [LIGHT_BLUE] * m + [WHITE] * (len1 - m)
    positions = [(i * WIDTH // (m + n), HEIGHT // 3) for i in range(len1)]
    draw_array(nums1, m, n, colors, positions)
    pygame.display.flip()
    time.sleep(1 / speed)

    while n > 0 and m > 0:
        screen.fill(WHITE)
        draw_background()

        if nums2[n-1] >= nums1[m-1]:
            explanation = f"Comparing {nums2[n-1]} from nums2 with {nums1[m-1]} from nums1. {nums2[n-1]} is larger, so it goes into nums1."
            display_explanation(explanation)
            animate_element_transition(positions[n-1 + m], positions[end_idx], nums2[n-1], GREEN, m, n)
            nums1[end_idx] = nums2[n-1]
            colors[end_idx] = GREEN
            n -= 1
        else:
            explanation = f"Comparing {nums2[n-1]} from nums2 with {nums1[m-1]} from nums1. {nums1[m-1]} is larger, so it stays in nums1."
            display_explanation(explanation)
            animate_element_transition(positions[m-1], positions[end_idx], nums1[m-1], LIGHT_BLUE, m, n)
            nums1[end_idx] = nums1[m-1]
            colors[end_idx] = LIGHT_BLUE
            m -= 1

        end_idx -= 1
        draw_array(nums1, m, n, colors, positions)
        pygame.display.flip()
        time.sleep(1 / speed)

    while n > 0:
        screen.fill(WHITE)
        draw_background()
        explanation = f"Remaining elements from nums2 are being placed in nums1."
        display_explanation(explanation)
        animate_element_transition(positions[n-1 + m], positions[end_idx], nums2[n-1], GREEN, m, n)
        nums1[end_idx] = nums2[n-1]
        colors[end_idx] = GREEN
        n -= 1
        end_idx -= 1
        draw_array(nums1, m, n, colors, positions)
        pygame.display.flip()
        time.sleep(1 / speed)

def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3

    playing = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    playing = not playing  # Toggle pause/play
                elif event.key == pygame.K_UP:
                    speed *= 2  # Increase speed
                elif event.key == pygame.K_DOWN:
                    speed /= 2  # Decrease speed

        if playing:
            screen.fill(WHITE)
            animate_merge(nums1, m, nums2, n)
            playing = False  # Pause after one run of animation
            time.sleep(3)

if __name__ == "__main__":
    main()
