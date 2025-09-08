for i in range(1, 13):
    print("No. {:<2} squared is {:<3} and cubed is {:<4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter your name: ")
age = int(input("Please enter your age, {}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote!")
    print("Please put X into the box")
else:
    print("Please come back again in {} years!".format(18 - age))

if age < 18:
    print("Please come back again in {} years!".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi!")
else:
    print("You are old enough to vote!")
    print("Please put X into the box")