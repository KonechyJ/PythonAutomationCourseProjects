#A guess the number name

import random

print("Hello player, What is your name?")
playerName = input()
print("Hello " + playerName + " Let's play a game. ")
print("I am thinking of a number between one and twenty.")
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 7):
    print("Take a guess player.")
    playerGuess = int(input())

    if playerGuess < secretNumber:
        print("Your guess is too low.")
    elif playerGuess > secretNumber:
        print("Your guess is too high.")
    else:
        break
if playerGuess == secretNumber:
    print("Good Job " + playerName + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope! The number I was thinking of was " + str(secretNumber))

