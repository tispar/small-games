import random
import time

#A method to display the intro text
def displayIntro():
    print()


#Asking user to choose cave 1 or 2 and return a sting with '1' or '2'
def chooseCave():
    cave = ''
    
    return cave

#Checking if the cave 
def checkCave(caveNumber):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    #determine if 1 or 2 is the "friendly" Cave

    #Check if the user has chosen the right cave and create an output

#Game Loop
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()