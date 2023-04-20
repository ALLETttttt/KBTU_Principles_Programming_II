from random import randint


def guess_the_number(name):
    n = randint(1, 20)
    j, amount = 0, 0
    while j != n:
        if j == 0:
            print(f'Well, {name}, I am thinking of a number between 1 and 20.')
            print('Take a guess.')
            j = int(input())
            amount += 1
        else:
            print('Your guess is too low.')
            print('Take a guess.')
            j = int(input())
            amount += 1

    print(f'Good job, {name}! You guessed my number in {amount} guesses!')


print('Hello! What is your name?')
name = input()
guess_the_number(name)