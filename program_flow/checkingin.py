parrot = "Norwegian Blue"

letter = input("Please enter a character: ")

if letter in parrot:
    print("{} is in {}.".format(letter, parrot))
else:
    print("I don't need that letter.")

activity = input("What do you want to do today? ")

if "cinema" not in activity.casefold():
    print("But i want to go to the cinema")