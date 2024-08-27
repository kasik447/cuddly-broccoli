'''
1. Display the board with 9 position for X and Y
2. Make sure the board is empty
3. Provide numbers for each cell so the players can refer to it
4. Provide error message for placing a symbol in a filled cell
5. If player has 3 symbols in a line, display "You Win" message.
'''

theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}

boardKeys = []

for key in theBoard:
    boardKeys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print('It is turn of ' + turn + ' Specify the place tou want to go')

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('Sorry this cell location is filled. Please Choose an other one.')
            continue

        if count >= 5:

            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game')
                break

        if count == 9:
            print('\nGame Over\n')
            print('The game is Tie!')

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input('Do you want to restart the Game? (y/n) ').lower()

    if restart == 'y':
        for key in boardKeys:
            theBoard[key] = ' '
        game()


if __name__ == '__main__':
    game()
