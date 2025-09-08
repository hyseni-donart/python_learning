albums = [
    ("Welcome to my nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("NightFlight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
    ]


for album in albums:
    name, artist, year = album
    print(f"Album: {name}, Artist: {artist}, Year: {year}")

for name, artist, year in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# metallica2 = list(metallica)
# print(metallica2)

# metallica2[0] = "Master of Puppets"
# print(metallica2)

# name, artist, year = metallica
# print(name)
# print(artist)
# print(year)

# table = ("Coffe Table", 200, 100, 75, 34.50)

# name, length, width, height, price = table
# print(length * width)