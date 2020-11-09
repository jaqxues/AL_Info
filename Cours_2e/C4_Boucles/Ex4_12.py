from random import randint

n = int(input('Enter n: '))
x = randint(1, n)

counter = 0
while True:
    guess = int(input(f'Guess ({counter}): '))
    counter += 1

    if guess == x:
        break
    elif guess < x:
        print('Too low')
    else:
        print('Too high')

print(f'Correct: x = {x}. {counter} guess(es)')
