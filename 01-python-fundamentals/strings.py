print("Today is a good day to learn Python!")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " " + "world!")

greeting = "Hello"
name = input("Please enter your name ")

print(greeting + name)

print(greeting + " " + name)

age = 24
print(age)

number = 10.0
print(number)

newNumber = 10j
print(newNumber)

print(type(age), type(number), type(newNumber))

age_in_words = "2 years"
print(age_in_words)

print(name + f"is {age} years old.")
print(type(age_in_words))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")