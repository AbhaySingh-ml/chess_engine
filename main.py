import pygame
import os

pygame.init()

from move_validation import is_valid_move
from check_logic import is_checkmate, is_in_check, find_king

# Initialize the screen dimensions
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('AI based Chess Engine')

# Load fonts for display
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

# Frame rate control
timer = pygame.time.Clock()
fps = 60

# Define RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Define board parameters
SQUARE_SIZE = 100
BOARD_TOP_LEFT = (
    (WIDTH - SQUARE_SIZE * 8) // 2,
    (HEIGHT - SQUARE_SIZE * 8) // 2
)

# Function to draw the 8x8 chess board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            square = pygame.Rect(
                BOARD_TOP_LEFT[0] + col * SQUARE_SIZE,
                BOARD_TOP_LEFT[1] + row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )
            pygame.draw.rect(screen, color, square)

# Initial placement of pieces on the board
starting_board = [
    ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook'],
    ['black_pawn'] * 8,
    [''] * 8,
    [''] * 8,
    [''] * 8,
    [''] * 8,
    ['white_pawn'] * 8,
    ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
]

# Load piece images from folder
piece_images = {}
base_path = r'D:\Chess engine project making\Engine\images'
colors = ['white', 'black']
pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']

for color in colors:
    for piece in pieces:
        filename = f'{color} {piece}.png'
        image_path = os.path.join(base_path, filename)
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        piece_images[f'{color}_{piece}'] = image

# Draw pieces on the board according to the state of 'board'
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '':
                x = BOARD_TOP_LEFT[0] + col * SQUARE_SIZE
                y = BOARD_TOP_LEFT[1] + row * SQUARE_SIZE
                screen.blit(piece_images[piece], (x, y))
        
# Highlight the selected piece square
def highlight_selected_square(square):
    if square:
        row, col = square
        rect = pygame.Rect(
            BOARD_TOP_LEFT[0] + col * SQUARE_SIZE,
            BOARD_TOP_LEFT[1] + row * SQUARE_SIZE,
            SQUARE_SIZE,
            SQUARE_SIZE
        )
        pygame.draw.rect(screen, (0, 255, 0), rect, 4)  # Green border

# Game state variables
selected_square = None
current_turn = 'white'
run = True

# Main game loop
while run:
    timer.tick(fps)
    screen.fill(WHITE)

    draw_board()
    draw_pieces(starting_board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = (mouse_x - BOARD_TOP_LEFT[0]) // SQUARE_SIZE
            row = (mouse_y - BOARD_TOP_LEFT[1]) // SQUARE_SIZE

            if 0 <= row < 8 and 0 <= col < 8:
                clicked_square = (row, col)
                piece = starting_board[row][col]

                if selected_square is None:
                    # Select the piece if it belongs to the current player
                    if piece != '' and piece.startswith(current_turn):
                        selected_square = clicked_square
                else:
                    # Try to move the selected piece
                    if is_valid_move(starting_board, selected_square, clicked_square, current_turn):
                        start_row, start_col = selected_square
                        end_row, end_col = clicked_square

                        target_piece = starting_board[end_row][end_col]

                        # Prevent illegal move: capturing the king
                        if target_piece != '' and target_piece.endswith('king'):
                            print("Illegal move: Cannot capture the king!")
                            selected_square = None
                            continue  # Skip rest of loop

                        # Move piece
                        starting_board[end_row][end_col] = starting_board[start_row][start_col]
                        starting_board[start_row][start_col] = ''

                        # Switch turn
                        current_turn = 'black' if current_turn == 'white' else 'white'

                        # Check game state
                        if is_in_check(starting_board, current_turn, is_valid_move):
                            print(f"{current_turn} is in check!")

                        if is_checkmate(starting_board, current_turn, is_valid_move):
                            print(f"Checkmate! {current_turn} loses.")
                            run = False  # Exit game loop

                    # Reset selection after move attempt
                    selected_square = None

    highlight_selected_square(selected_square)
    pygame.display.flip()

pygame.quit()
