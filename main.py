#i need to create a board
def create_board(board):
    for i in board:
        for j in i:
            print(j, end = ' ')
        print('\n')

def return_board():
    row = [['*'] * 3] * 3
    return row

def pvp():
    board = return_board()
    run = True
    while run:
        create_board(board)
        player1_choice = input('O or X: ').lower()
        player1_index = int(input("Enter a number from 1 to 9: "))
        player1_index += 1
        if player1_index > 3:
            row = player1_index % 3
            col = player1_index - row
            board[row][col] = player1_choice
        create_board(board)
        player2_choice = input('O or X: ').lower()
        player2_index = int(input("Enter a number from 1 to 9: "))
        player2_index += 1
        if player2_index > 3:
            row = player1_index % 3
            col = player1_index - row - 1
            board[row][col] = player2_choice
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
