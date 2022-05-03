import random
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
    ===''','''
 +---+
[0   |
/|\  |
/ \  |
    ===''','''
 +---+
[0]  |
/|\  |
/ \  |
    ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pidgeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    #Diese Funktion gibt einen zufällig ausgewählten String aus der übergebenen Liste zurück.
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
    # Gibt True zurück, wenn der Spieler noch einmal spielen möchte, andernfalls False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #Lässt den Spieler einen Buchstaben eingeben.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Prüft ob der Spieler gewonnen hat.
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

        #Prüft ob der der Spieler zu oft geraten und verloren hat.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!/nAfter ' + str(len(missedLetters)) +' missed guesses and ' + str(len(correctLetters)) + ' correct guesses.\n The word was "' + secretWord + '".')
            gameIsDone = True

    #Fragt, ob der Spieler erneut spielen möchte (nur wenn das Spiel beendet ist).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
