#i need to create a board
def create_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def return_board():
    row = ['-', '-', '-',
           '-', '-', '-',
           '-', '-', '-']
    return row


def player_input(board, player_choice):
    while True:
        try:
            player_index = int(input(f"Enter a number from 1 to 9 to place your {player_choice}: ")) - 1
            if player_index < 0 or player_index > 8:
                print("Invalid input! Please enter a number from 1 to 9.")
                continue
            if board[player_index] != '-':
                print(f"Position {player_index + 1} is already marked!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number from 1 to 9.")
    board[player_index] = player_choice.upper()
    create_board(board)
    return player_index


def win_or_lose(board, player_choice, player_index):
    win = False
    win_condn = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
                 [0, 4, 8], [2, 4, 6]]
    for i in win_condn:
        if player_index in i:
            if board[i[0]] == board[i[1]] == board[i[2]] == player_choice.upper():
                win = True
                break

    return win



def pvp():
    board = return_board()
    player_choice = input('Player-1, choose O or X: ').upper()
    while player_choice not in ['O', 'X']:
        print('Invalid choice! Please enter either O or X.')
        player_choice = input('Player-1, choose O or X: ').upper()

    p1 = player_choice
    p2 = 'X' if p1 == 'O' else 'O'

    current_player = 1
    while True:
        if current_player == 1:
            print("Player-1's turn")
            player_index = player_input(board, p1)
            if win_or_lose(board, p1, player_index):
                print("Player-1 wins!")
                break
            current_player = 2
        else:
            print("Player-2's turn")
            player_index = player_input(board, p2)
            if win_or_lose(board, p2, player_index):
                print("Player-2 wins!")
                break
            current_player = 1

        if '-' not in board:
            print("It's a tie!")
            break


def main():
    print("Welcome to Tic Tac Toe!")
    print("What mode would you like to play?:")
    print("    1.PvP")
    print("    2.PvE(AI)")
    print('\n')
    mode = int(input())
    if mode == 1:
        pvp()


main()
