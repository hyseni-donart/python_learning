def multiply(x, y):
    result = x * y
    return result

answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

for value in range(1, 5):
    two_times = multiply(2, value)
    print(two_times)

def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    
    return is_palindrome(string)


word = input("Please enter a palindrome: ")
if palindrome_sentence(word):
    print(f"'{word}' is a Palindrome")
else:
    print(f"'{word}' is not a Palindrome")