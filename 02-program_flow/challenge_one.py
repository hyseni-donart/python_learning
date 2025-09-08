name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age < 18 or age > 31:
    print("Sorry, our holidays are only for cool people.")
else:
    print("Welcome to club 18-30 holiday, {}".format(name))