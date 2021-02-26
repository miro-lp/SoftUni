from project.song import Song
from project.album import Album
from project.band import Band

song = Song("Running in the 90s", 3.45, False)
song_1 = Song("Running in the 80s", 3.65, False)
print(song.get_info())
album = Album("Initial D", song, song_1)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

