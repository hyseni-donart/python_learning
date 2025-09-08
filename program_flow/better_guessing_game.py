import random
highest = 1000

answer = random.randint(1, highest)

print("Please guess number between 1 to {}: ".format(highest))
guess = int(input())

if guess != answer:
    while guess != answer:
        if guess == 0:
            print("Game Over")
            break
        elif guess < answer:
            print("Please guess higher ")
            guess = int(input())
        elif guess > answer:
            print("Please guess lower ")
            guess = int(input())
    print("You guessed it!")
else:
    print("You got it first time!")

#--------------------------------------------------------------------------
answer = random.randint(1, highest)
guess = 0
print("Please guess number between 1 to {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print("Well done you guessed it")
    else:
        if guess < answer:
            print("guess higher")
        else:
            print("guess lower")