n = int(input())
songs = {}
for i in range(n):
    name, *info_song = input().split("|")
    songs[name] = info_song
while True:
    line = input()
    if line == "Stop":
        break
    command, piece, *others = line.split("|")
    if command == "Add":
        if piece in songs:
            print(f"{piece} is already in the collection!")
        else:
            print(f"{piece} by {others[0]} in {others[1]} added to the collection!")
            songs[piece] = others
    elif command == "Remove":
        if piece not in songs:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            songs.pop(piece)
    elif command == "ChangeKey":
        if piece not in songs:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Changed the key of {piece} to {others[0]}!")
            songs[piece][1] = others[0]
songs = dict(sorted(songs.items(), key=lambda x: (x[0], x[1][0])))

for i in songs:
    print(f"{i} -> Composer: {songs[i][0]}, Key: {songs[i][1]}")
