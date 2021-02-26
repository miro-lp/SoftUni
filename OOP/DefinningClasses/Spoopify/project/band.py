from .album import Album


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name not in [a.name for a in self.albums]:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        for a in self.albums:
            if a.name == album_name:
                if a.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(a)
                    return f"Album {album_name} has been removed."
        if album_name not in [a.name for a in self.albums]:
            return f"Album {album_name} is not found."

    def details(self):
        name_info = f"Band {self.name}"
        album_info = "\n".join([f"{a.details()}" for a in self.albums])
        if len(self.albums)>0:
            return name_info + "\n" + album_info + "\n"
        else:
            return name_info + "\n"
