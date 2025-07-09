import copy
# Position of the king
def find_king(board, color):
    king_name = f'{color}_king'
    for row in range(8):
        for col in range(8):
            if board[row][col] == king_name:
                return (row, col)
    return None

def is_in_check(board, color, is_valid_move_func):
    king_pos = find_king(board, color)
    opponent = 'black' if color == 'white' else 'white'

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '' and piece.startswith(opponent):
                if is_valid_move_func(board, (row, col), king_pos, opponent):
                    return True
    return False

def is_checkmate(board, color, is_valid_move_func):
    if not is_in_check(board, color, is_valid_move_func):
        return False

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '' and piece.startswith(color):
                for r in range(8):
                    for c in range(8):
                        if is_valid_move_func(board, (row, col), (r, c), color):
                            new_board = copy.deepcopy(board)
                            new_board[r][c] = new_board[row][col]
                            new_board[row][col] = ''
                            if not is_in_check(new_board, color, is_valid_move_func):
                                return False
    return True
