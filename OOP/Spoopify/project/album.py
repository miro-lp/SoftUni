from .song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        else:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            else:
                if song.name not in [i.name for i in self.songs]:
                    self.songs.append(song)
                    return f"Song {song.name} has been added to the album {self.name}."
                else:
                    return "Song is already in the album."

    def remove_song(self, song: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            if song in [i.name for i in self.songs]:
                for s in self.songs:
                    if s.name == song:
                        self.songs.remove(s)
                        break
                return f"Removed song {song} from album {self.name}."
            else:
                return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        name_info = f"Album {self.name}"
        album_info = "\n".join([f"== {s.get_info()}" for s in self.songs])
        if len(self.songs) > 0:
            return name_info + "\n" + album_info + "\n"
        else:
            return name_info + "\n"
