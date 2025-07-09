AI Based chess engine

A Python-based chess engine with a graphical interface using Pygame, featuring basic move validation, piece selection, and an AI opponent (coming soon). This project is a personal learning endeavor into game development, artificial intelligence, and Python.



Project Overview

This is a chess engine developed using Python. The aim is to:

Create a functional GUI for the chessboard and pieces

Implement legal move validation

Add turn-based mechanics

Develop a basic AI for automated moves

Explore search algorithms like Minimax and Alpha-Beta pruning (future scope).





&nbsp;Recommended Learning Path (Step-by-Step)

**📘 Phase 1: Build a Simple Chess Engine (No AI)**

* Write a board representation (you can use FEN).(Done)
* Implement move generation (or use python-chess library).(done)
* Build a basic engine that picks random or rule-based moves.(done)



**📘 Phase 2: Add Minimax + Alpha-Beta (Classic Search)**

* Implement evaluation functions.
* Add depth-limited search using Minimax.
* Optimize with Alpha-Beta pruning.

✅ This gives you a rule-based chess engine. Now move to RL.



**🔁 Phase 3: Reinforcement Learning**

Here’s what to do:

**🧪 Step 1: Setup Training Environment**

* Use python-chess as the game environment.
* Design the RL agent (inputs: board state; outputs: move probabilities).
* Reward function: +1 for win, -1 for loss, 0 for draw.



**🧠 Step 2: Choose RL Algorithm**

* Start with Deep Q-Learning (DQN) or Policy Gradient.
* Later, explore AlphaZero-like architecture (uses Monte Carlo Tree Search + Neural Net).



**🏋️ Step 3: Train Your Agent**

* Start with self-play (play games against itself).
* Save training data (board, move, result).
* Train your neural net to predict good moves.



**🧪 Step 4: Evaluate and Improve**

* Test it vs random or rule-based bots.
* Track win rate and loss.
* Adjust reward function or model architecture.



**🛠️ Libraries \& Tools**

python-chess: board handling, move generation.

PyTorch / TensorFlow: training neural networks.

Ray RLlib (optional): scalable RL training.

Stockfish: can use for benchmarking.







### **Complete Chess Move Rules to Implement**

**1. Basic Movement Rules**

✅ Pawn: one step forward, two on first move, diagonal capture(Done)

✅ Knight: L-shaped moves (2+1)

✅ Bishop: diagonal movement

✅ Rook: straight lines (horizontal/vertical)

✅ Queen: straight + diagonal (rook + bishop)

✅ King: one step in any direction



**2. Special Rules**

✅ Castling (King + Rook move)

* King and rook haven’t moved
* No pieces in between
* King not in check, and doesn't pass through check



✅ En Passant

* When a pawn moves 2 squares forward and lands next to an opponent pawn
* Opponent pawn can capture it as if it moved 1 square forward
* Only valid on the immediate next move



✅ Pawn Promotion

* When pawn reaches last rank (8th for white, 1st for black)
* Must be promoted to Queen, Rook, Bishop, or Knight (usually Queen)



**3. Game State Rules**

✅ Check

The King is under attack

The current player must respond by:

* Moving the King
* Blocking the check
* Capturing the attacking piece



✅ Checkmate

The King is under check and has no valid moves to escape

Ends the game



✅ Stalemate

No legal moves, but the King is not in check

Game ends in a draw



✅ Draw Conditions

Fifty-move rule: no pawn move or capture in 50 moves

Threefold repetition: same board state 3 times

Insufficient material: not enough pieces to checkmate (e.g., K vs K, or K+B vs K)



**4. Turn-Based Mechanics**

✅ Enforce alternate turns between White and Black

✅ Prevent moving opponent’s pieces















