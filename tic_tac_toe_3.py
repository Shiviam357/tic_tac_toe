"""
Tic-Tac-Toe Version 3: The UX and AI Foundation
Upgrade: UX Improvement through clear screen function.
This version ensures the board stays in one place in the terminal,
mocking a real digital game interface.
"""

import os

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    # 'nt' is for Windows; 'posix' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    """Clears the screen and prints the 3x3 board."""
    clear_screen()
    print("--- Tic-Tac-Toe V3 ---")
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---+---+---")

def check_win(board):
    """Checks rows, columns, and diagonals for a winner."""
    # Check Rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return True
            
    # Check Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return True
            
    # Check Diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
        
    return False

def play_game():
    # Initializing 2D array
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    current_player = "X"
    turns = 0

    while turns < 9:
        display_board(board)
        
        # Move validation loop
        while True:
            try:
                choice = int(input(f"Player {current_player}, choose a spot (1-9): "))
                # Mapping 1-9 to 2D coordinates [row][col]
                row = (choice - 1) // 3
                col = (choice - 1) % 3
                
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col].isdigit():
                    break
                else:
                    input("Invalid move! Press Enter to try again...")
                    display_board(board)
            except ValueError:
                input("Please enter a number. Press Enter to try again...")
                display_board(board)

        # Update board
        board[row][col] = current_player
        turns += 1

        # Check for win
        if check_win(board):
            display_board(board)
            print(f"\nPlayer {current_player} wins! 🏆")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("\nIt's a draw! 🤝")

if __name__ == "__main__":
    play_game()