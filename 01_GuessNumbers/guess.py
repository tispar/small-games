# This is a number guessing game
import random 

guessesTaken = 0

#Getting the name of the user
print('Hello! What is your name?')
myName = input()

#Setting the random number for the user to guess
number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

#Asks for up to 6 times for a number input of the user 
for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    #Feedback
    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    #Exit loop if user guessed the right number
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
