import pygame
import threading
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mutating 3D Form")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colors = [WHITE, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Shape class
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.size = random.randint(50, 100)
        self.color = random.choice(colors)
        self.angle = 0
        self.mutation_speed = random.uniform(0.01, 0.05)
        self.splitting = False

    def mutate(self):
        while not self.splitting:
            self.size += random.uniform(-1, 1)
            self.angle += self.mutation_speed
            pygame.time.wait(10)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x - self.size < 0 or self.x + self.size > width:
            self.vx = -self.vx
        if self.y - self.size < 0 or self.y + self.size > height:
            self.vy = -self.vy

    def draw(self):
        points = []
        for i in range(6):
            angle = self.angle + math.radians(i * 60)
            x = self.x + self.size * math.cos(angle)
            y = self.y + self.size * math.sin(angle)
            z = self.size * math.sin(angle)
            points.append((x, y))
        # Draw 3D effect
        pygame.draw.polygon(screen, self.color, points)
        darker_color = tuple(max(0, c - 50) for c in self.color)
        for point in points:
            pygame.draw.line(screen, darker_color, (self.x, self.y), point)

    def split(self, line_start, line_end):
        self.splitting = True
        half_size = self.size / 2
        angle = random.uniform(0, 2 * math.pi)
        offset_x = half_size * math.cos(angle)
        offset_y = half_size * math.sin(angle)
        child1 = Shape(self.x + offset_x, self.y + offset_y)
        child2 = Shape(self.x - offset_x, self.y - offset_y)
        return child1, child2

# List of shapes
shapes = [Shape(width // 2, height // 2)]
threads = []

# Start mutation threads
for shape in shapes:
    thread = threading.Thread(target=shape.mutate)
    threads.append(thread)
    thread.start()

running = True
drawing = False
line_start = None

def line_intersects_shape(line_start, line_end, shape):
    # Basic intersection logic
    for i in range(6):
        angle = shape.angle + math.radians(i * 60)
        x1 = shape.x + shape.size * math.cos(angle)
        y1 = shape.y + shape.size * math.sin(angle)
        x2 = shape.x + shape.size * math.cos(shape.angle + math.radians((i+1) * 60))
        y2 = shape.y + shape.size * math.sin(shape.angle + math.radians((i+1) * 60))

        denom = ((line_end[0] - line_start[0]) * (y2 - y1)) - ((line_end[1] - line_start[1]) * (x2 - x1))
        if denom == 0:
            continue
        ua = (((x2 - x1) * (line_start[1] - y1)) - ((y2 - y1) * (line_start[0] - x1))) / denom
        ub = (((line_end[0] - line_start[0]) * (line_start[1] - y1)) - ((line_end[1] - line_start[1]) * (line_start[0] - x1))) / denom

        if 0 <= ua <= 1 and 0 <= ub <= 1:
            return True
    return False

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            line_start = pygame.mouse.get_pos()
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            line_end = pygame.mouse.get_pos()
            drawing = False
            if line_start:
                for shape in shapes:
                    if shape.splitting:
                        continue
                    if line_intersects_shape(line_start, line_end, shape):
                        child1, child2 = shape.split(line_start, line_end)
                        shapes.remove(shape)
                        shapes.extend([child1, child2])
                        thread1 = threading.Thread(target=child1.mutate)
                        thread2 = threading.Thread(target=child2.mutate)
                        threads.extend([thread1, thread2])
                        thread1.start()
                        thread2.start()
                        break
            line_start = None

    screen.fill(BLACK)

    for shape in shapes:
        shape.move()
        shape.draw()

    pygame.display.flip()

pygame.quit()
