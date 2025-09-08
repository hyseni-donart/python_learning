# 1. Check if a number is positive, negative, or zero.

num = int(input("Please enter a number: "))

if num < 0:
    print(f"The number {num} is a negative number")
elif num == 0:
    print(f"The number {num} is zero")
else:
    print(f"The number {num} is a positive number")

# 2. Check if a number is even or odd.

num = int("Please enter a number: ")

if num % 2 == 0:
    print(f"The number {num} is an even number")
else:
    print(f"The number {num} is an odd number")

# 3. Ask for a password and print “Access Granted” if it matches a secret one.

password = input("Please enter your password: ")
secret_Pasword = "Norwegian Blue"

if password == secret_Pasword:
    print("Access Granted")
else:
    print("Wrong Password")

# 4. Ask for a user's age and print if they are a child, teen, or adult.

age = int(input("Please enter your age: "))

if age >= 0 and age < 10:
    print("Child")
elif age >= 10 and age < 20:
    print("Teen")
elif age < 0:
    print("If this is your age you aren't born yet")
else:
    print("Adult")

# 5. Take a name and print it in all uppercase.

name = input("Please enter your age: ")

print(name.upper())

# 6. Take a sentence and count how many characters it has.

parrot = "Norwegian"

print(len(parrot))

# 7. Ask for a number and check if it’s between 10 and 20.

num = int(input("Please enter a number: "))

if num >= 10 and num <= 20:
    print("correct")
else:
    print("incorrect")

# 8. Print "YES" if a string contains the word "Python".

word = input("Please enter a word: ")

if "Python" not in word:
    print("No")
else:
    print("Yes")

# 9. Check if a word starts with a capital letter.

word = input("Please enter a word: ")

if word[0].isupper():
    print("Yes")
else:
    print("No")

# 10. Ask for a word and print it backwards.

word = input("Please enter a word: ")

print(word[::-1])

# 11. Ask for a sentence and count how many times the letter “e” appears.

sentence = input("Please enter a sentence: ")

print(sentence.count("e"))

# 12. Replace all spaces in a string with underscores.

word = input("Please enter a word: ")

print(word.replace(" ", ","))

# 13. Ask for a sentence and print it without vowels.

sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
result = ""

for char in sentence:
    if char not in vowels:
        result += char

print(result)

# 14. Take a string and print True if it contains both “a” and “b”.

word = input("Please enter a word: ")

if "a" not in word and "b" not in word:
    print("False")
else:
    print("True")

# 15. Ask for a word and check if it's a palindrome (same forward and backward).

word = input("Please enter a word: ")

if word == word[::-1]:
    print("True")
else:
    print("False")

# 16. Ask for a sentence and print the number of words in it.

sentence = input("Please enter a sentence: ")
words = sentence.split()

print(len(words))

# 17. Loop through numbers 1 to 20 and print only the even ones.

for i in range(1, 20):
    if i % 2 == 0:
        print(i)
    else:
        print()

# 18. Print all characters in a string one by one.

word = "Norwegian Blue"

for char in word:
    print(char)

# 19. Ask for a number and print all numbers from 1 to that number.

num = int(input("Please enter a number: "))

for i in range(1, num + 1):
    print(i)

# 20. Print numbers from 1 to 50 that are divisible by 5.

for i in range(1, 50):
    if i % 5 == 0:
        print(i)

# 21. Ask for a word and print each letter with its index (ex: A is at position 0).

word = input("Please enter a word: ")
index = 0

for char in word:
    print(f"The letter {char} is at index {index}")
    index += 1

# 22. Print the first 10 square numbers (1, 4, 9, 16...).

for i in range(1, 11):
    print(i ** 2)

# 23. Print all words from a sentence that are longer than 4 letters.

sentence = input("Please enter a sentence: ")
words = sentence.split()
print(words)

for words in sentence:
    if len(word) > 4:
        print(words)

# 24. Count how many vowels are in a word.

word = input("Please enter a word: ")
vowels = "aeiouAEIOU"
num = 0

for char in word:
    if char in vowels:
        num += 1

print(num)

# 25. Ask for a list of words (separated by commas) and print them in reverse order.

word_List = input("Please enter a list of words: ")
words = word_List.split()

for words in word_List:
    print(words[::-1])