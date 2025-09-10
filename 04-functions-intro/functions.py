def multiply(x: float, y: float) -> float:
    """
    Multiply to numbers together.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    Args:
        x (int or float): The first number to multiply.
        y (int or float): The number to multiply `x` by.

    Returns:
        (int or float): The product of `x` and `y`.
    """
    result = x * y
    return result

# answer = multiply(10.5, 4)
# print(answer)

# forty_two = multiply(6, 7)
# print(forty_two)

# for value in range(1, 5):
#     two_times = multiply(2, value)
#     print(two_times)

def is_palindrome(string: str) -> bool:
    """
    Check if the string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.


    Args:
        string (str): The string to check.

    Returns:
        (bool): True if `string` is a palindrome, false otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if the string is a palindrome.

    This function removes all non-alphanumeric characters
    form the input sentence and then checks if the 
    remaining characters form a palindrome, ignoring case.

    Args:
        sentence (str): The string to check.

    Returns:
        (bool): True if `string` is a palindrome, false otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    
    return is_palindrome(string)


# word = input("Please enter a palindrome: ")
# if palindrome_sentence(word):
#     print(f"'{word}' is a Palindrome")
# else:
#     print(f"'{word}' is not a Palindrome")

def fibonacci(n: int) -> int:
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(36):
    print(i, fibonacci(i))

p = is_palindrome("bob")
print(p)