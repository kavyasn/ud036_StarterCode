import webbrowser

class Movie():
    '''
    This class contains the properties of a movie including movie title, 
    storyline, poster image, and a YouTube link to the movie trailer.
    '''
    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        '''
        :param title: String constaining the name of the movie
        :param storyline: String containing the synopsis of the movie
        :param poster_image_url: URL of the jpg image 
        :param trailer_youtube_url: Link to the trailer on YouTube. 
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        param: self
        Upon invoking, this function opens the YouTube trailer of the Movie object
        '''
        webbrowser.open(self.trailer_youtube_url)
