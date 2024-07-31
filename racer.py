import pygame
import sys
import openai
import json
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)

# Piece symbols
PIECES = {
    'wp': 'P', 'wr': 'R', 'wn': 'N', 'wb': 'B', 'wq': 'Q', 'wk': 'K',
    'bp': 'P', 'br': 'R', 'bn': 'N', 'bb': 'B', 'bq': 'Q', 'bk': 'K'
}

# Draw board
def draw_board(win):
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces
def draw_pieces(win, board):
    font = pygame.font.SysFont('Arial', 44)
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != '--':
                piece_text = font.render(PIECES[piece], True, BLUE if piece[0] == 'w' else RED)
                win.blit(piece_text, (col * SQUARE_SIZE + SQUARE_SIZE//4, row * SQUARE_SIZE + SQUARE_SIZE//4))

# Draw HUD
def draw_hud(win, player_turn, ai_thinking, ai_move=None, last_move=None):
    font = pygame.font.SysFont('Arial', 24)
    hud_text = f"Turn: {'White' if player_turn == 'white' else 'Black (AI)'}"
    hud_surface = font.render(hud_text, True, GRAY)
    win.blit(hud_surface, (10, 10))

    if ai_thinking:
        thinking_text = "AI is thinking..."
        thinking_surface = font.render(thinking_text, True, GRAY)
        win.blit(thinking_surface, (10, 40))

    if ai_move:
        move_text = f"AI Move: {ai_move[0]} to {ai_move[1]}"
        move_surface = font.render(move_text, True, GRAY)
        win.blit(move_surface, (10, 70))

    if last_move:
        last_move_text = f"Last Move: {last_move}"
        last_move_surface = font.render(last_move_text, True, GRAY)
        win.blit(last_move_surface, (10, 100))

# Convert board to JSON representation
def board_to_json(board):
    board_dict = {"board": board}
    return json.dumps(board_dict)

# Convert chess coordinates to board indices
def coord_to_index(coord):
    col = ord(coord[0]) - ord('a')
    row = 8 - int(coord[1])
    return row, col

# Convert board indices to chess coordinates
def index_to_coord(row, col):
    return f"{chr(col + ord('a'))}{8 - row}"

# Function to call OpenAI API for the next move
def make_next_move(board):
    board_json = board_to_json(board)

    function = {
        "type": "function",
        "function": {
            "name": "make_next_move",
            "description": "Get the next move in the chess game for the black side",
            "parameters": {
                "type": "object",
                "properties": {
                    "piece_current_coordinate": {
                        "type": "string",
                        "description": "The current coordinate of the piece, e.g., 'e2'",
                    },
                    "piece_move_to_coordinate": {
                        "type": "string",
                        "description": "The coordinate to move the piece to, e.g., 'e4'",
                    },
                },
                "required": ["piece_current_coordinate", "piece_move_to_coordinate"],
            },
        }
    }

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful chess assistant."},
            {"role": "user", "content": f"Here is the board configuration:\n{board_json}\nWhat is the next move?"}
        ],
        tools=[function],
        tool_choice="auto"
    )

    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
        tool_call = tool_calls[0]
        function_args = json.loads(tool_call.function.arguments)
        return function_args.get("piece_current_coordinate"), function_args.get("piece_move_to_coordinate")
    return None, None

# Main game loop
def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess')
    board = [
        ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
        ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
    ]
    running = True
    player_turn = 'white'
    selected_piece = None
    ai_thinking = False
    ai_move = None
    last_move = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                if selected_piece:
                    from_square = index_to_coord(selected_piece[0], selected_piece[1])
                    to_square = index_to_coord(row, col)
                    last_move = f"{from_square}-{to_square}"
                    board[row][col] = board[selected_piece[0]][selected_piece[1]]
                    board[selected_piece[0]][selected_piece[1]] = '--'
                    selected_piece = None
                    player_turn = 'black'
                else:
                    if board[row][col] != '--' and (board[row][col][0] == 'w' if player_turn == 'white' else board[row][col][0] == 'b'):
                        selected_piece = (row, col)

        if player_turn == 'black' and not ai_thinking:
            ai_thinking = True
            from_square, to_square = make_next_move(board)
            if from_square and to_square:
                from_row, from_col = coord_to_index(from_square)
                to_row, to_col = coord_to_index(to_square)
                last_move = f"{from_square}-{to_square}"
                board[to_row][to_col] = board[from_row][from_col]
                board[from_row][from_col] = '--'
                ai_move = (from_square, to_square)
                player_turn = 'white'
            ai_thinking = False

        draw_board(win)
        draw_pieces(win, board)
        draw_hud(win, player_turn, ai_thinking, ai_move, last_move)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
