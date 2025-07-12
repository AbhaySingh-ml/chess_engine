# **AI Based chess engine**

A Python-based chess engine with a graphical interface using Pygame, featuring basic move validation, piece selection, and an AI opponent (coming soon). This project is a personal learning endeavor into game development, artificial intelligence, and Python.



# **Project Overview**

This is a chess engine developed using Python. The aim is to:

1. Create a functional GUI for the chessboard and pieces
2. Implement legal move validation
3. Add turn-based mechanics
4. Develop a basic AI for automated moves
5. Explore search algorithms like Minimax and Alpha-Beta pruning (future scope).

For each possible square on the board (0-7 x 0-7):

Check if it's a valid move (your existing is_valid_move)

Then simulate that move (copy board, make the move)

Run is_in_check() on the new board

If the king is still in check — discard that move

Only keep the moves that defend or remove the check




