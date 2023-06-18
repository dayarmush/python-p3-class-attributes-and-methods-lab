class Song:

    artist_count = {}
    genre_count = {}
    artists = []
    genres = []
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    def add_song_to_count(self):
        Song.count += 1

    def add_to_genres(self, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)


    def add_to_artists(self, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    def add_to_genre_count(self, genre):
            Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
            return Song.genre_count

    def add_to_artist_count(self, artist):
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

        return Song.artist_count
        


