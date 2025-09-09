import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin)

    The function will continue looping and prompting
    the user, until a valid `int` is entered.

    Args:
        prompt: The string that the user will see, when
        they're prompted to enter the value.
    Returns:
        return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        #     print(f"'{temp}' is not a valid number")
        print(f"'{temp}' is not a valid number")
        


highest = 1000

# answer = random.randint(1, highest)

# print("Please guess number between 1 to {}: ".format(highest))
# guess = get_integer(": ")

# if guess != answer:
#     while guess != answer:
#         if guess == 0:
#             print("Game Over")
#             break
#         elif guess < answer:
#             print("Please guess higher ")
#             guess = int(input())
#         elif guess > answer:
#             print("Please guess lower ")
#             guess = int(input())
#     print("You guessed it!")
# else:
#     print("You got it first time!")

#--------------------------------------------------------------------------
print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
#--------------------------------------------------------------------------
help(get_integer)
#--------------------------------------------------------------------------
answer = random.randint(1, highest)
guess = 0
print("Please guess number between 1 to {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

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