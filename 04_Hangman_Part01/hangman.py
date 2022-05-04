import random
# Program flow chart
#                 +---------+
#                 |         |
#                 |  START  <---------------------------------+
#                 |         |                                 |
#                 +----+----+                                 |
#                      |                                      |
#              +-------v--------+                             |
#              |                |                             |
#       +------> Chooses a word |                             |
#       |      |                |                             |
#       |      +-------+--------+                             |
#       |              |                                      |
#       |      +-------v--------+       +--------------+      |
#       |      |                +------->              |      |
#       |      | Ask Player to  |       |Player already|      |
#       |      | guess a letter |       |guessed this  |      |
#       |      |                <-------+   letter     |      |
#       |      +----+--------+--+       +--------------+      |
#       |           |        |                                |
#+------+--------+  |        |  +---------------+             |
#|  Word does    <--+        +--> Word does not |             |
#|contain letter |              |contain letter |             |
#+------+--------+              +-------+-------+             |
#       |                               |                     |
#       |                               |                     |
#+------v--------+              +-------v---------+           |
#| Word complete |              |All guesses taken|           |
#|  Player wins  |              |  Player loses   |           |
#+------+--------+              +-------+---------+           |
#       |                               |                     |
#       |        +--------------+       |                     |
#       |        |Ask Player if |       |                     |
#       +-------->he/she wants  <-------+                     |
#                |to play again |                             |
#                +-----+--------+-----------------------------+
#                      |
#                   +--v----+
#                   |       |
#                   |  END  |
#                   |       |
#                   +-------+

#List containing the hangman pics
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 0   |
     |
     |
    ===''','''
 +---+
 0   |
 |   |
     |
    ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
 +---+
 0   |
/|\  |
     |
    ===''','''
 +---+
 0   |
/|\  |
/    |
    ===''','''
 +---+
 0   |
/|\  |
/ \  |
    ===''']

#list of possible words, feel free to add more animals
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pidgeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    #This function returns a random string-element from the given List
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #Ersetzt Unterstriche durch die korrekt erratenen Buchstaben
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Zeigt das Wort mit Leerzeichen zwischen den Buchstaben an.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #GIbt den eingegebenen Buchstaben zurück. Diese Funktion sorgt dafür, dass nur ein Buchstabe und nichts anderes eingegeben wird.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #Asks the player if he wants to play again an returns True if the answer is yes (False if not)
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

#Initialize game
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    #your primary gameplay loop
    displayBoard(missedLetters, correctLetters, secretWord)

    #get a letter from the player
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Checks if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Check if the player has exceeded his guesses and lost the game
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!/nAfter ' + str(len(missedLetters)) +' missed guesses and ' + str(len(correctLetters)) + ' correct guesses.\n The word was "' + secretWord + '".')
            gameIsDone = True

    #Ask the player if he wants to play again (if the game is done)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break