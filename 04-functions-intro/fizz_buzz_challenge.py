def fizz_buzz(num: int) -> str:
    """
    Returns 'Fizz' if num is divisible by 3, 'Buzz' if
    divisible by 5, 'Fizz Buzz' if divisible by both and
    the number itself if undivisible by neither.

    Args:
        num (int): the number to check

    Returns:
        str: 'Fizz', 'Buzz', 'Fizz Buzz' or the number as a string.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
    

input("Play Fizz Buzz.    Press ENTER to start.")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print(f"You lose, the correct answer was {correct_answer}")
        break
else:
    print(f"Well done, you reached {next_number}")


# def factorial(n: int) -> int:
#     """
#     Return n! (0! is 1).
 
#     Valid for `n` in the range 0 to 998 (inclusive).
#     Larger values of `n` will cause a RecursionError.
#     """
#     if n <= 1:
#         return 1
 
#     return n * factorial(n - 1)


# for i in range(36):
#     print(i, factorial(i))

# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
 
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
 
#     return result
 
 
# for i in range(36):
#     print(i, factorial(i))
