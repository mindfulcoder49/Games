import pygame
import random
import time
import sys
import openai
from dotenv import load_dotenv
import os
import threading
from math import cos, sin

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Programming Statements Typing Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Font
font = pygame.font.Font(None, 36)

# Starfield background effect
stars = []
for _ in range(200):
    stars.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3)])

# Game variables
falling_statements = []
input_text = ""
score = 0
lives = 5
game_over = False
show_message = False
message_text = ""
streaming_response = ""
starfield_angle = 0

# Configurable parameters
statements_per_minute = 4
base_statement_speed = 1
current_code_index = 0

def create_new_statement():
    global current_code_index
    if current_code_index >= len(user_code):
        current_code_index = 0
    text = user_code[current_code_index].strip()
    current_code_index += 1
    x = random.randint(0, WIDTH - font.size(text)[0])
    y = -font.size(text)[1]
    fall_speed = base_statement_speed / (0.1 * len(text) + 1)
    return {"text": text, "x": x, "y": y, "speed": fall_speed}

def draw_text(text, x, y, color):
    screen.blit(font.render(text, True, color), (x, y))

def draw_starfield():
    global starfield_angle
    starfield_angle += 0.1
    if starfield_angle > 360:
        starfield_angle = 0
    for star in stars:
        star[1] += star[2]  # Speed depends on star size
        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = random.randint(-20, -1)
        rotated_star = rotate_point(star[0], star[1], WIDTH // 2, HEIGHT // 2, starfield_angle)
        pygame.draw.line(screen, WHITE, rotated_star, (rotated_star[0], rotated_star[1] + 10), 1)

def rotate_point(x, y, cx, cy, angle):
    radians = angle * (3.14159 / 180)
    dx, dy = x - cx, y - cy
    new_x = dx * cos(radians) - dy * sin(radians) + cx
    new_y = dx * sin(radians) + dy * cos(radians) + cy
    return (new_x, new_y)

def explain_code(current_line):
    global streaming_response
    context_before = "\n".join(user_code[max(0, current_code_index-11):current_code_index-1]).strip()
    context_after = "\n".join(user_code[current_code_index:min(len(user_code), current_code_index+10)]).strip()
    current_line = current_line.strip()

    prompt = f"""
    Here are the ten lines previous to the one the user just typed, if they exist:
    {context_before}
    Here is the code the user just typed:
    {current_line}
    Here are the next ten lines of code:
    {context_after}
    Provide a single sentence explanation of the line the user just typed given its context. Provide only a single sentence.
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        stream=True
    )
    
    streaming_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            streaming_response += chunk.choices[0].delta.content
            display_message(streaming_response)
            time.sleep(0.1)  # Adjust delay as necessary

def display_message(text):
    global show_message, message_text
    show_message = True
    message_text = text
    pygame.time.set_timer(pygame.USEREVENT, 8000)  # Display for 8 seconds

def draw_text_wrapped(message_text, x, y, color, font, max_width):
    words = message_text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    
    lines.append(current_line)  # Add the last line

    for i, line in enumerate(lines):
        draw_text(line, x, y + i * font.get_linesize(), color)

def start_explain_thread(statement):
    explain_thread = threading.Thread(target=explain_code, args=(statement["text"],))
    explain_thread.start()

if len(sys.argv) < 2:
    print("Usage: python game.py <code_file>")
    sys.exit(1)

code_file = sys.argv[1]
with open(code_file, 'r') as f:
    user_code = f.readlines()

# Main game loop
clock = pygame.time.Clock()
statement_interval = 60 / statements_per_minute
last_statement_time = time.time()  # Initialize to the current time

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    falling_statements = []
                    score = 0
                    lives = 5
                    statements_per_minute = 4
                    base_statement_speed = 1
                    current_code_index = 0
            else:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    for statement in falling_statements:
                        if input_text == statement["text"].strip():
                            falling_statements.remove(statement)
                            score += 1
                            input_text = ""
                            start_explain_thread(statement)
                            break
                    else:
                        input_text = ""
                else:
                    input_text += event.unicode
        elif event.type == pygame.USEREVENT:
            show_message = False
            pygame.time.set_timer(pygame.USEREVENT, 0)

    if not game_over:
        draw_starfield()

        current_time = time.time()
        if current_time - last_statement_time >= statement_interval:
            falling_statements.append(create_new_statement())
            last_statement_time = current_time

        for statement in falling_statements:
            statement["y"] += statement["speed"]
            if statement["y"] > HEIGHT:
                falling_statements.remove(statement)
                lives -= 1
                if lives <= 0:
                    game_over = True

        for statement in falling_statements:
            draw_text(statement["text"].strip(), statement["x"], statement["y"], RED)

        draw_text(f"Score: {score}", 10, 10, WHITE)
        draw_text(f"Lives: {lives}", WIDTH - 100, 10, WHITE)
        draw_text(input_text, WIDTH // 2 - font.size(input_text)[0] // 2, HEIGHT - 40, GREEN)
        
        statement_interval = 60 / statements_per_minute
    else:
        draw_text("Game Over!", WIDTH // 2 - font.size("Game Over!")[0] // 2, HEIGHT // 2 - 20, RED)
        draw_text("Press Enter to Restart", WIDTH // 2 - font.size("Press Enter to Restart")[0] // 2, HEIGHT // 2 + 20, RED)

    if show_message:
        max_width = WIDTH - 40  # Set your desired maximum width
        draw_text_wrapped(message_text, 20, HEIGHT // 2 - 20, YELLOW, font, max_width)

    pygame.display.flip()
    clock.tick(30)
