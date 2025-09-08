# 1. Print your name and age on separate lines.

name = "Donart"
age = 19

print(name + "\n" + str(age))

# 2. Store your city and favorite number in variables and print:
# "I live in [City] and my favorite number is [Number]."

city = "Vushtrri"
number = 7

print("I live in", city, "and my favorite number is", number)

# 3. Concatenate your first and last name with a space in between.

name = "Donart"
lastName = "Hyseni"
fullName = name + " " + lastName

print(fullName)

# 4. Get user's name using input(), and greet them with "Hello, [name]!"

userName = input("Please enter your name: ")

print("Hello, " + userName + "!")

# 5. Convert age from string to integer and add 5 years.

age = "19"

print(int(age) + 5)

# 6. Ask for two numbers (as input), convert to float, and print the sum.

a = input("Please enter a number: ")
b = input("Please enter a number again: ")
c = float(a) + float(b)

print(c)

# 7. Print the last 3 characters of a string using slicing.

parrot = "Norwegian Blue"

print(parrot[-3:])

# 8. Ask the user to enter a sentence, and print the sentence in reverse.

sentence = input("Please enter a sentence: ")

print(sentence[::-1])

# 9. Slice a string to print every second character.

name = "Donart Hyseni"

print(name[::2])

# 10. Get the price of a product and quantity, calculate total cost. 

price = 12.40
quantity = 23
totalCost = quantity * price

print(totalCost)

# 11. Ask for a 4-digit number (as string), print each digit on a new line.

stringNumber = input("Please enter a 4-digit number: ")

print(int(stringNumber[0]))
print(int(stringNumber[1]))
print(int(stringNumber[2]))
print(int(stringNumber[3]))

# 12. Take a string and float, and print the string repeated int(float) times.

string = "Hello "
num = 3.0
result = string * int(num)

print(result)

# 13. Ask user for a word and a number, and slice the word using that number as the end index.

word = input("Please enter a word: ")
number = int(input("Please enter a number: "))

print(word[:number])