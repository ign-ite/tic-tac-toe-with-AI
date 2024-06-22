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

def player_input(board):
    player1_choice = input('O or X: ').lower()
    if player1_choice != 'o' and player1_choice != 'x':
        print('Please enter either o or x')
        player_input(board)
    player1_index = int(input("Enter a number from 1 to 9: "))
    player1_index -= 1
    board[player1_index] = player1_choice.upper()
    # create_board(board)
    # player2_choice = input('O or X: ').lower()
    # player2_index = int(input("Enter a number from 1 to 9: "))
    # player2_index -= 1
    # board[player2_index] = player2_choice
    create_board(board)
def pvp():
    board = return_board()
    run = True
    while run:
        player_input(board)

def win_or_lose():
    
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
