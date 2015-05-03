# media.py
#
# Description:
# Defines a custom movie object with the relevant attributes
#
# Author: Ross Gynn
# Version: 1.0 [2015-04-28]

# Standard python class imports
import webbrowser

class Movie():
    def __init__(self,
                 movie_title,
                 movie_year,
                 movie_director,
                 movie_stars,
                 movie_description,
                 movie_poster,
                 movie_trailer,
                 movie_imdb):
        
        # On init create instance variables from the above arguments
        self.title = movie_title
        self.year = movie_year
        self.director = movie_director
        self.starring = movie_stars
        self.storyline = movie_description
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.imdb_url = movie_imdb
        
    # Method to open the movie trailer directly in the browser
    def play_trailer(self):
        webbrowser.open(self.trailer_url)
  
