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
    player_index = int(input("Enter a number from 1 to 9: "))
    if board[player_index] == player_choice:
        print(f"{player_choice} is already marked!")
        player_input(board, player_choice)
    player_index -= 1
    win = False
    win_condn = []
    for i in range(0, 9):
        if i == player_index:
            if i % 3 == 0:
                if board[i+1] == player_choice and board[i+2] == player_choice:
                    win = True
                elif board[i+3]
    if player_index == 0:
        if board[1] == player_choice and board[2] == player_choice:
            win = True
        elif board[4] == player_choice and board[8] == player_choice:
            win = True
        elif board[3] == player_choice and board[6] == player_choice:
            win = True
    elif player_index == 1:
        if board[0] == player_choice and board[2] == player_choice:
            win = True
        elif board[4] == player_choice and board[7] == player_choice:
            win = True
    elif player_index == 2:
        if board[1] == player_choice and board[0] == player_choice:
            win = True
        elif board[5] == player_choice and board[8] == player_choice:
            win = True
        elif board[4] == player_choice and board[6] == player_choice:
            win = True
    board[player_index] = player_choice.upper()
    create_board(board)


def pvp():
    board = return_board()
    run = True
    while run:
        player_turn(board)


def player_turn(board):
    player_choice = input('O or X: ').lower()
    if player_choice != 'o' and player_choice != 'x':
        print('Please enter either o or x')
        board = return_board()
        player_turn(board)
    p1 = player_choice
    if player_choice == 'o':
        p2 = 'X'
    else:
        p2 = 'O'
    print("Player-1")
    player_input(board, p1)
    print("Player-2")
    player_input(board, p2)


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
