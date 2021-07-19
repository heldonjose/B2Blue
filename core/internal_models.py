class Serie(object):
    def __init__(self, map):
        self.title = map['name']
        self.img = map['backdrop_path']
        self.overview = map['overview']
        self.year = str(map['first_air_date']).split('-')[0]
        self.first_air_date = map['first_air_date']
        self.popularity = map['popularity']