for index, character in enumerate("abcdefgh"):
    print(index, character)

for t in enumerate("abcdefg"):
    index, character = t
    print(index, character)

index, item = (0, "a")
print(index)
print(item)
