# Initialize the board as a list of 9 empty strings
board = [" " for _ in range(9)]

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_player_move(player_symbol):
    """Gets a valid move from the current player."""
    while True:
        try:
            move = int(input(f"Player {player_symbol}, enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                return move
            else:
                print("Invalid move. Please choose an empty spot between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player_symbol):
    """Checks if the given player has won."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player_symbol for i in combo):
            return True
    return False