'''
1. Change the number range 1 to 1 000 000
2. Game should ask us to guess a number
3. Give a clue of the number is higher or lower than the guess
4. Inform the player if he won
'''


from random import randint

start, end = 1, 1000
value = randint(start, end)

print(f'The computer choose a number between {start} and {end}')

guess = None

while guess != value:
    guess = int(input('Guess the number: '))

    if guess < value:
        print('The number is Higher')
    elif guess > value:
        print('The number is Lower')

print('Congratulations!!! You guess the number. You won.')
