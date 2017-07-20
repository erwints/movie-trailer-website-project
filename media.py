import webbrowser #module for displaying web-based documents

class Movie():
    """Creates the Movie class to create instances of movies.

    Attributes:
        movie_title: A string indicating the title of the movie.
        poster_image: A string of the image url.
        trailer_youtube: A string of the trailer url.
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Constructor for Movie - creates the instances and sets the values
        of each instance"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """calls open() in the webbrowser module to display a trailer in the
        browser"""
        webbrowser.open(self.trailer_youtube_url)
