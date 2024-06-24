def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_win(board, player):
    """Checks if the current player has won."""
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    return [player, player, player] in win_conditions


def available_moves(board):
    """Returns a list of available (empty) cells on the board."""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves


def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)


def minimax(board, depth, alpha, beta, maximizing_player):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif is_draw(board):
        return 0

    moves = available_moves(board)

    if maximizing_player:
        best_score = -float('inf')
        for move in moves:
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, alpha, beta, False)
            board[move[0]][move[1]] = ' '
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        least_score = float('inf')
        for move in moves:
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, alpha, beta, True)
            board[move[0]][move[1]] = ' '
            least_score = min(least_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return least_score


def best_move(board):
    best_score = -float('inf')
    move = None
    for m in available_moves(board):
        board[m[0]][m[1]] = 'X'
        score = minimax(board, 0, -float('inf'), float('inf'), False)
        board[m[0]][m[1]] = ' '
        if score > best_score:
            best_score = score
            move = m
    return move


def main():
    """Main function to play the game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    current_player = 'O'

    while True:
        if current_player == 'O':
            player_move = tuple(map(int, input("Enter your move (row and column): ").split()))
            if board[player_move[0]][player_move[1]] == ' ':
                board[player_move[0]][player_move[1]] = 'O'
                current_player = 'X'
            else:
                print("Invalid move. Try again.")
                continue
        else:
            # AI's move with Alpha-Beta Pruning
            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = 'X'
            current_player = 'O'

        print_board(board)

        if check_win(board, 'O'):
            print("Congratulations! You won!")
            break

        if check_win(board, 'X'):
            print("AI wins!")
            break

        if len(available_moves(board)) == 0:
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()
