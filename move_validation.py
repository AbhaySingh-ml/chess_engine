import copy
# Move validation and legal moves
def is_valid_move(board, from_pos, to_pos, current_turn):
    from_row, from_col = from_pos
    to_row, to_col = to_pos

    piece = board[from_row][from_col]
    target = board[to_row][to_col]

    if piece == '' or not piece.startswith(current_turn):
        return False

    if target != '' and target.startswith(current_turn):
        return False

    piece_type = piece.split('_')[1]
    row_diff = to_row - from_row
    col_diff = to_col - from_col

    if piece_type == 'pawn':
        direction = -1 if current_turn == 'white' else 1
        start_row = 6 if current_turn == 'white' else 1

        if col_diff == 0:
            if row_diff == direction and board[to_row][to_col] == '':
                return True
            if from_row == start_row and row_diff == 2 * direction and board[from_row + direction][from_col] == '' and board[to_row][to_col] == '':
                return True
        elif abs(col_diff) == 1 and row_diff == direction and target != '' and not target.startswith(current_turn):
            return True

    elif piece_type == 'rook':
        if from_row == to_row or from_col == to_col:
            return is_clear_path(board, from_pos, to_pos)

    elif piece_type == 'bishop':
        if abs(row_diff) == abs(col_diff):
            return is_clear_path(board, from_pos, to_pos)

    elif piece_type == 'queen':
        if from_row == to_row or from_col == to_col or abs(row_diff) == abs(col_diff):
            return is_clear_path(board, from_pos, to_pos)

    elif piece_type == 'knight':
        if (abs(row_diff), abs(col_diff)) in [(2, 1), (1, 2)]:
            return True

    elif piece_type == 'king':
        if abs(row_diff) <= 1 and abs(col_diff) <= 1:
            return True

    return False

# This function ensures that a piece like a rook, bishop, or queen does not jump over other pieces when moving in a straight or diagonal line.
def is_clear_path(board, from_pos, to_pos):
    from_row, from_col = from_pos
    to_row, to_col = to_pos

    row_step = (to_row - from_row) // max(1, abs(to_row - from_row)) if from_row != to_row else 0
    col_step = (to_col - from_col) // max(1, abs(to_col - from_col)) if from_col != to_col else 0

    cur_row = from_row + row_step
    cur_col = from_col + col_step

    while (cur_row, cur_col) != (to_row, to_col):
        if board[cur_row][cur_col] != '':
            return False
        cur_row += row_step
        cur_col += col_step

    return True

