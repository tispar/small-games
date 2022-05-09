#The game Tic-Tac-Toe
import random as rd
import time

#Draws the board based on a list with the length of 9
def displayBoard(board):
    print(
    f'''| {board[0]} | {board[1]} | {board[2]} |
----+---+----
| {board[3]} | {board[4]} | {board[5]} |
----+---+----
| {board[6]} | {board[7]} | {board[8]} |''')
    print("")
    
# Asks the player which cell he wants to fill out, checks is cell is available
def getInput(board,counter):
    #Handle user Input
    while True:
        print("Please choose a cell (1-9)")
        cell = input()
        if cell not in "1 2 3 4 5 6 7 8 9".split():
            print("Please enter a number between 1 and 9")
        else:
            cell = int(cell)
            break
    
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

def inputMachine(board):
    while True:
        move = rd.randint(1,9)
        time.sleep(rd.randint(1,4))
        if board[move-1] == move:
            board[move-1] = "O"
            print("I choose cell number "+ str(move))
            break
        else:
            print("thinking...")

def inputSkynet(board):
    winList = ['O','O']
    #TODO Check board for winning moves
    if winPossible(board) != 0:
        move = winPossible
        board[move - 1] = "O"
    #TODO Check board for sabotage
    #elif
    #Take the middle
    elif board[4] == '5':
        board[4] = "O"
    #random
    else:
        inputMachine(board)

def winPossible(board):
    chunk = []
    winList = ['O','O']
    boardCopy = [str(x) for x in board]
    #Zeilen
    for i in range(0,3):
        chunk.append(boardCopy[i:i+3])
        if set(chunk[1:]) == set(winList):
            return int(chunk[0])
        chunk = []
    #Spalten
    for i in range(0,3):
        chunk = boardCopy[i::3].sort()
        print(chunk)
        if set(chunk[1:]) == set(winList):
            return int(chunk[0])
    #Diagonalen
    chunk = boardCopy[::4].sort()
    if set(chunk[1:]) == set(winList):
            return int(chunk[0])
    chunk = boardCopy[2:8:2].sort()
    if set(chunk[1:]) == set(winList):
            return int(chunk[0])
    return 0
    
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
        print("Tic Tac Toe - Main Menu")
        print("")
        print("1 - Human vs Human")
        print("2 - Human vs Machine")
        print("3 - Human vs Skynet (Does not work. ... yet :)")
        print("4 - Exit")
        print("")
        while True:
            print("Please choose an option")
            i = input()
            if i not in "1 2 3 4".split():
                print("Please enter a number between 1 and 4")
            else:
                i= int(i)
                break
        #End the Application
        if i == 4:
            print("Goodbye")
            break

        #Human vs Human
        elif i == 1:
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
        
        #Human vs Machine
        elif i == 2:
            while True:
                print("Welcome to a new round of Tic-Tac-Toe!")
                while counter < 10:
                    displayBoard(board)
                    if counter % 2 == 1:
                        getInput(board, counter)
                    else:
                        inputMachine(board)

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
        #Human vs Skynet
        elif i == 3:
            while True:
                print("Welcome to a new round of Tic-Tac-Toe!")
                while counter < 10:
                    displayBoard(board)
                    if counter % 2 == 1:
                        getInput(board, counter)
                    else:
                        inputSkynet(board)

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