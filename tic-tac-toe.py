def print_board(board):
    print("\n")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("\n")

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))
        
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Please enter a valid row and column.")
            continue
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That cell is already occupied. Try again.")
            continue
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()