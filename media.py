""" Contains the class Movie which is used to create objects of different movies """

# Defining a class movie as a blueprint for all movies to be added
class Movie(object):
    """Class Movie contains a single constructor that is used to initialize instances
       by assigning values to the class variables """
       
    # Automatically called whenever an object is created!
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
