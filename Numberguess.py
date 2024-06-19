import random
import math

lower = int(input('Enter lower range '))
upper = int(input('Enter upper range '))

number = random.randint(lower, upper)

guesses = round(math.log(upper - lower + 1, 2))

while(guesses):
    guess = int(input('Guess the number '))
    if(guess == number):
        print('Congratulations! You guessed it right')
        exit()
    elif(guess < number):
        print('Try Again! You guessed too small')
    else:
        print('Try Again! You guessed too high')
    guesses = guesses - 1

print('Better Luck Next Time!')