import random

print('Hello! What is your name?')
name = input()

print(name + ' it is nice to meet you.')
print('I\'m thinking of a number between 1 and 20. Can you guess it?')

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess!')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job ' + name + '! You guessed the number correctly in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking was: ' + str(secretNumber))
