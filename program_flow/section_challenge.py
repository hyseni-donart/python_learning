choice = "-"
while choice != "0":
    if choice in "12345":
        print("Your choice was {}".format(choice))
    else:
        print("Please chose your option from the list below: ")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tGo Swimming")
    print("4:\tHave Dinner")
    print("5:\tGo to bed")
    print("0:\tExit")
    choice = input()

