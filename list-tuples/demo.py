albums = [
    ("Welcome to my nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
      [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready Fo Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Chose"),
         (7, "Movin' on"),
         (8, "Seagull"),
     ]
     ),
    ("NightFlight", "Budgie", 1981,
       [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She used me Up"),
     ]
     ),
    ("More Mayhem", "Emilda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Keltish Town Waltz"),
     ]
     ),
    ]

SONGS_LIST = 3
SONG_TITLE = 1  

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST]
    else:
        break 

    print("Choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")
    
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE]
    else:
        break

    print(f"Playing {title}")
    print("=" * 40)