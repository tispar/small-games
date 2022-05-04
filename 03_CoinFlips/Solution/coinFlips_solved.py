#import random
import random

#Print out string asking the player his guess of 1000 throws and ask for an input to start the game
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()

flips = 0
heads = 0

#while loop 
while flips < 1000:
    #determine result of coinflip and count if heads
    if random.randint(0,1) == 1:
        heads = heads + 1
    #increase number of flips
    flips = flips + 1

    #print interim results
    if flips == 900:
        print('900 flips and there have been ' + str(heads) + ' heads.')
    if flips == 100:
        print('100 flips and there have been ' + str(heads) + ' heads.')
    if flips == 500:
        print('500 flips and there have been ' + str(heads) + ' heads.')

print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times.')
print('Were you close?')
