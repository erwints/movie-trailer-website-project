import webbrowser #module for displaying web-based documents

#creates a class called Movie()
class Movie():
    # this is a class contructor which uses the __init__ method to initialize
    # all the date associated with the instance using the keyword "self"
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # calls open() in the webbrowser module to display a trailer in the browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
