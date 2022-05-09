#The game Tic-Tac-Toe

#Draws the board based on a list with the length of 9
def displayBoard(board):
    print(
    f'''| {board[0]} | {board[1]} | {board[2]} |
----+---+----
| {board[3]} | {board[4]} | {board[5]} |
----+---+----
| {board[6]} | {board[7]} | {board[8]} |''')
    


# Asks the player which cell he wants to fill out, checks is cell is available
def getInput(board,counter):

    #TODO what happens when user enters sth else than 1-9 ?
    print("Please choose a cell (1-9)")
    cell = int(input())

    if board[cell-1] == cell:
        if counter % 2 != 0: 
            board[cell-1] = 'X' 
        else:
            board[cell-1] = 'O'
    else:
        print("Cell already taken")
        getInput(board,counter)

#Checks if the active player has won
def winner(board,counter):
    clist = []
    if counter % 2 != 0: 
        clist = ['X', 'X', 'X'] 
    else:
        clist = ['O', 'O', 'O'] 
 
    if (
    board[0:3] == clist or board[3:6] == clist or board[6:8] == clist or 
    board[::3] == clist or board[1::3] == clist or board[2::3] == clist or 
    board[::4] == clist or board[2:8:2] == clist
    ):
        return True
    else: 
        return False

#Asks the player if he wants to play again an returns True if the answer is yes (False if not)
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# Tic-tac-toe game
if __name__ == "__main__":
    
    #Initialize values
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counter = 1
    
    # Start a new round of Tic-tac-toe
    while True:  
        print("Welcome to a new round of Tic-Tac-Toe!")
    
        #Game loop
        while counter < 10:
            displayBoard(board)
            getInput(board, counter)
            if winner(board,counter):
                displayBoard(board)
                print(f"We have a winner after {counter} turns:")
                break
            counter += 1
    
        if not winner(board,counter):
            displayBoard(board)
            print("Game is a draw!")
        
        if playAgain():
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            counter = 1
        else:
            break