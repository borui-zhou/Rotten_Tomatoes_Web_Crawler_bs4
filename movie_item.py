class Movie_item:
  def __init__(self, name, rating, tomatometer, rotten, fresh, studio, director, genre, in_theater_year, cast,number_of_cast, runtime):
    self.name = name
    self.rating = rating
    self.tomatometer = tomatometer
    self.fresh = fresh
    self.studio = studio
    self.rotten = rotten
    self.director = director
    self.genre = genre
    self.in_theater_year = in_theater_year
    self.cast = cast
    self.number_of_cast = number_of_cast
    self.runtime = runtime

  def asdict(self):
    return {'name': self.name,
            'rating': self.rating,
            'tomatometer': self.tomatometer,
            'fresh': self.fresh,
            'studio': self.studio,
            'rotten': self.rotten,
            'director': self.director,
            'genre': self.genre,
            'in_theater_year': self.in_theater_year,
            'cast': self.cast,
            'number_of_cast':self.number_of_cast,
            'runtime':self.runtime}
