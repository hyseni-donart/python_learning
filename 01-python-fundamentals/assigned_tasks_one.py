# Challenge 1: Type Detector
# Ask the user to enter any value. Print the type of the value using type().

word = "Hello"
number = 14
anotherNumber = 13.0

print(type(word), type(number), type(anotherNumber))

# Challenge 2: Basic Math
# Create a small script that adds two numbers and prints the result.

a = 13
b = 28
c = a + b

print(c)

# Challenge 3: Expression Game
# Evaluate and print the result of the expression:
# 3 + 4 * 2 - (1 + 2)

print(3 + 4 * 2 - (1 + 2))

# Challenge 4: First and Last Character
# Ask the user for a word. Print the first and the last character using indexing.

word = input("Please enter a word: ")

print(word[0], word[-1])

# Challenge 5: Secret Code
# Given a string, print every second character using slicing.
# Example: "HelloWorld" → "Hlool"

word = "Hello World"

print(word[::2])

# Challenge 6: Reverse a String
# Take a string input and print it in reverse using slicing.

word = "Hello World"

print(word[::-1])

# Challenge 7: String + Math
# Ask for the user's name and their age. Then print a sentence like:
# "Hello Arben, next year you will be 21."

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print("Hello " + name + ", next year you will be", str(age) + ".")

# Challenge 8: Extract Date Parts
# Given a string in format "2025-07-25", extract and print:

# The year

# The month

# The day
# (using slicing)

date = "2025-07-25"

print(date[0:4])
print()
print(date[5:7])
print()
print(date[8:])

# Challenge 9: Operator Precedence Game
# Write a few expressions and ask the student to predict the result before running the code.

print(2 + 3 * 4)        # 14
print((2 + 3) * 4)      # 20
print(10 / 2 + 5 * 2)   # 15.0

# Challenge 10: Slice That Word
# Ask the user for a word and two numbers: start and end.
# Use slicing to print the substring from index start to end.

word = input("Please enter a word: ")
firstNum = int(input("Please enter a number: "))
secondNum = int(input("Please enter another number: "))

print(word[firstNum:secondNum])