import random
n = random.randint(1,10)
guess = 0
while guess != n:
    guess = int(input('Guess a number'))
    if guess < n:
        print('It is smaller')
    elif guess > n:
        print('It is larger')
    else:
        print('correct guess')

