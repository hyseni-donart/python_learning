# 1. Print your full name using an f-string.

name = "Donart"

print(f"My name is {name}")

# 2. Ask the user for their favorite food and print: "I love [food] too!"

favFood = input("Please enter your favorite food: ")

print("I love {0} too!".format(favFood))

# 3. Create a sentence using .format() with 2 placeholders (name and hobby).

name = "Donart"
hobby = "coding"

print("My name is {0} and my hobby is {1}!".format(name, hobby))

# 4. Ask the user for their first name and print how many characters it has.

name = input("Please enter your name: ")

print(len(name))

# 5.Use string multiplication to print "Hi " 10 times.

print("Hi " * 10)

# 6. Ask the user for two numbers and print their difference.

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = a - b

print(c)

# 7. Print the float number 3.14159 with only 2 decimal places using formatting.

pi = 3.14159

print("PI is approximately {0:.2f}".format(pi))

# 8. Print "Hello" with each character on a new line using slicing.

word = "Hello"

print(word[0] + "\n" + word[1] + "\n" + word[2] + "\n" + word[3] + "\n" + word[4])

# 9. Get a string input and check if it contains "python" (case insensitive).

word = input("Please enter some words: ")

print("python" in word)

# 10. Create a string and print it centered in a 30-character wide space.

word = "Hello World!"

print("{0:^30}".format(word))

# 11. Ask the user to input a number and print its square using f-string.

num = int(input("Please enter a number: "))

print("{0}".format(num ** 2))

# 12. Slice and print the last word of the sentence "Python is amazing".

words = "Python is amazing"
sliced_words = words[10:]

print(sliced_words)

# 13. Ask for two numbers and print a formatted string showing their sum, difference, and product.

a = int(input("Please enter a number:"))
b = int(input("Please enter another number:"))

print("The sum is {0} the difference is {1} and the product is {2}".format(a + b, a - b, a * b))

# 14. Slice and reverse only the middle three characters of "ABCDEFGHI".

word = "ABCDEFGHI"

print(word[3:6])

# 15. Print the first name and last name in a tabular format using escape characters.

firstName = "Donart"
lastName = "Hyseni"

print("{0}\t{1}".format(firstName, lastName))