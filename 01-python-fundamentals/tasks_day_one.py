# 1. Print your name and age on separate lines

name = "Donart"
age = 19

print(name + "\n" + str(age))

# 2. Store your name, age, and favorite color in variables, then print them in one sentence.
# Example: My name is John, I'm 25 years old, and I like blue.

name = "Donart"
age = 19
favorite_color = "Black"

print("My name is " + name + ", I'm " + str(age) + " years old, and I like " + favorite_color + ".")

# 3. Get the user's name using input() and greet them by name.
# Example: "Hello, [name]!"

name = input("Please enter your name: ")

print("Hello, " + name + "!")

# 4. Check the type of the variable price = 9.99 using type() and print it.

price = 9.99

print(type(price))

# 5. Print a file path: C:\Users\YourName\Documents — using escape characters so it prints correctly.

file_path = "C:\\Users\\YourName\\Documents"

print(file_path)

# 6. Ask the user for their age, convert it to an integer, and print how old they’ll be in 5 years.

age = int(input("Please enter your age: "))

print(age + 5)

# 7. Print a multiline poem or quote using \n to make it appear on different lines.

print("""I write in lines, both short and neat,
In silent rooms, on tired feet.
The screen glows soft, a guiding light,
I chase the code into the night.

A variable, a whispered name,
A loop that spins a gentle game.
Each bug a riddle, sharp and sly,
Each fix a cheer, a coding high.

Escape through slashes, \\n and \\t,\\n
My thoughts become reality.
From prints to types, from strings to flow,
With every run, I learn and grow.

So let the world spin loud and fast—
I’ll sit with Python, unsurpassed.
For in each line and logic bend,
I find a path, a thought, a friend.""")


print("I write in lines, both short and neat,\nIn silent rooms, on tired feet.\nThe screen glows soft, a guiding light,\nI chase the code into the night.\n\nA variable, a whispered name,\nA loop that spins a gentle game.\nEach bug a riddle, sharp and sly,\nEach fix a cheer, a coding high.\n\nEscape through slashes, \\n and \\t,\\n\nMy thoughts become reality.\nFrom prints to types, from strings to flow,\nWith every run, I learn and grow.\n\nSo let the world spin loud and fast—\nI’ll sit with Python, unsurpassed.\nFor in each line and logic bend,\nI find a path, a thought, a friend.")


# 8. Use escape characters to format this output:
# Name:   John
# Age:    24
# Email:  john@example.com

print("Name:\tJohn\nAge:\t24\nEmail:\tjohn@example.com")

# 9. Ask the user to enter two numbers (as input), convert them to float, add them, and print the result.

a = float(input("Please enter a number: "))
b = float(input("Please enter a number: "))
c = a + b 

print(c)

# 10. Ask the user for their birth year, calculate their age, and print it along with its data type.

birthYear = int(input("Please enter your year of birth: "))
currentYear = 2025
age = currentYear - birthYear

print(age, type(age))

# 11. Mini Data Formatter Tool:
# Ask the user to input name, age, and city

# Use a function to format it nicely like:
# Hello, my name is Sarah.
# I am 23 years old.
# I live in Berlin.
# Use \n, variables, input(), and function design together.

name = input("Please Enter Your Name: ")
age = int(input("Please enter your age: "))
city = input("Please enter your city")

print("Hello, my name is ", name, ".\nI am ", age, " years old.\nI live in ", city, ".")