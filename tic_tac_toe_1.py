# Tic-Tac-Toe Version 1: Basic Build
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = "X"
turns = 0

def display_board():
    """Prints the current state of the board."""
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")

print("Welcome to Tic-Tac-Toe V1!")

while turns < 9:
    display_board()
    
    # Inner loop to ensure we get a valid move
    while True:
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): "))
            index = choice - 1
            
            # Check if the move is within range and the spot isn't taken
            if 0 <= index <= 8 and board[index].isdigit():
                break
            else:
                print("Invalid move! Spot taken or out of range. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

    # Update board and count turn
    board[index] = current_player
    turns += 1
    
    # Win Logic (Checking all 8 combinations)
    if (board[0]==board[1]==board[2]) or (board[3]==board[4]==board[5]) or (board[6]==board[7]==board[8]) or \
       (board[0]==board[3]==board[6]) or (board[1]==board[4]==board[7]) or (board[2]==board[5]==board[8]) or \
       (board[0]==board[4]==board[8]) or (board[2]==board[4]==board[6]):
        display_board()
        print(f"Congratulations! Player {current_player} wins! 🎉")
        break
    
    # Switch players
    current_player = "O" if current_player == "X" else "X"
else:
    display_board()
    print("It's a draw! 🏁")