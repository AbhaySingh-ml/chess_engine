import pygame
import os
pygame.init()
from move_validation import is_valid_move
from check_logic import is_checkmate, is_in_check, find_king


# Creating basic temeplate of chess Board 
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('AI based chess engine')

# Fonts and timer
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)


# Board parameters
SQUARE_SIZE = 100
BOARD_TOP_LEFT = (
    (WIDTH - SQUARE_SIZE * 8) // 2,
    (HEIGHT - SQUARE_SIZE * 8) // 2
)

# code to draw the board of the chess  basic template
def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            # color = WHITE if (row + col) % 2 == 0 else BLACK
            square = pygame.Rect(
                BOARD_TOP_LEFT[0] + col * SQUARE_SIZE,
                BOARD_TOP_LEFT[1] + row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE
            )
            pygame.draw.rect(screen, color, square)

# placement of pieces
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

# Dictionary to hold all piece images
piece_images = {}
base_path = r'D:\Chess engine project making\Engine\images'

# Pieces list (matches file names exactly)
colors = ['white', 'black']
pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']

for color in colors:
    for piece in pieces:
        filename = f'{color} {piece}.png'  
        image_path = os.path.join(base_path, filename)
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        piece_images[f'{color}_{piece}'] = image  

# This function is drawing the chess pieces on the board.
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '':
                x = BOARD_TOP_LEFT[0] + col * SQUARE_SIZE
                y = BOARD_TOP_LEFT[1] + row * SQUARE_SIZE
                screen.blit(piece_images[piece], (x, y))

# This Function highlight the selected piece
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


selected_square = None
current_turn = 'white'  # Alternates between 'white' and 'black'
run = True
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
                    # Select if the piece belongs to current turn
                    if piece != '' and piece.startswith(current_turn):
                        selected_square = clicked_square
                else:
                    # # Try to move

                    if is_valid_move(starting_board, selected_square, clicked_square, current_turn):
                        start_row, start_col = selected_square
                        end_row, end_col = clicked_square

                    # Prevent capturing the king
                        target_piece = starting_board[end_row][end_col]
                    if target_piece != '' and target_piece.endswith('king'):
                        print("Illegal move: Cannot capture the king!")
                        selected_square = None
                        continue  # Skip to the next iteration of the loop

                        # Apply the move
                    starting_board[end_row][end_col] = starting_board[start_row][start_col]
                    starting_board[start_row][start_col] = ''

                    # Switch turn
                    current_turn = 'black' if current_turn == 'white' else 'white'

                        # Check for check or checkmate after switching turn
                    if is_in_check(starting_board, current_turn, is_valid_move):
                        print(f"{current_turn} is in check!")

                    if is_checkmate(starting_board, current_turn, is_valid_move):
                        print(f"Checkmate! {current_turn} loses.")
                        run = False  # Ends the game loop



                    # Reset selection either way
                    selected_square = None

    highlight_selected_square(selected_square)
    pygame.display.flip()



