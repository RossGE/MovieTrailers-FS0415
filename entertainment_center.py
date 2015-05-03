# entertainment_center.py
#
# Description:
# Defines a list of 6 favourite movies and their related attributes, and passes
# them to Udacity's fresh_tomatoes.py module for displaying as a HTML page
#
# Author: Ross Gynn
# Version: 1.0 [2015-04-28]

# Custom class imports
# Provided by Udacity for parsing movies and generating HTML/CSS to display
import fresh_tomatoes
# Created during Python Fundamentals course, defines a movie object
import media

# Define each of my favourite movies and their attributes
heat = media.Movie(
    "Heat",
    "1995",
    "Michael Mann",
    "Robert De Niro, Al Pacino, Val Kilmer",
    "DeNiro and Pacino tear it up!",
    "http://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Heatposter.jpg/220px-Heatposter.jpg",
    "https://www.youtube.com/watch?v=0xbBLJ1WGwQ",
    "http://www.imdb.com/title/tt0113277/"
)

gladiator = media.Movie(
    "Gladiator",
    "2000",
    "Ridley Scott",
    "Russel Crowe, Joaquin Phoenix, Oliver Reed",
    "Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the TRUE emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=ol67qo3WhJk",
    "http://www.imdb.com/title/tt0172495/"
)

district_9 = media.Movie(
    "District 9",
    "2009",
    "Neill Blomkamp",
    "Sharlto Copley, Jason Cope", 
    "An extraterrestrial race forced to live in slum-like conditions on Earth suddenly finds a kindred spirit in a government agent who is exposed to their biotechnology.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/d/d7/District_nine_ver2.jpg/220px-District_nine_ver2.jpg",
    "https://www.youtube.com/watch?v=DyLUwOcR5pk",
    "hhttp://www.imdb.com/title/tt1136608/"
)

alien = media.Movie(
    "Alien",
    "1979",
    "Ridley Scott",
    "Sigourney Weaver, John Hurt, Tom Skerritt",
    "The commercial vessel Nostromo receives a distress call from an unexplored planet. After searching for survivors, the crew heads home only to realize that a deadly bioform has joined them.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Alien_movie_poster.jpg/220px-Alien_movie_poster.jpg",
    "https://www.youtube.com/watch?v=LjLamj-b0I8",
    "http://www.imdb.com/title/tt0078748/"
)

twelve_monkeys = media.Movie(
    "Twelve Monkeys",
    "1995",
    "Terry Gilliam",
    "Bruce Willis, Brad Pitt",
    "Follows the journey of a time traveler from the post-apocalyptic future who appears in present day on a mission to locate and eradicate the source of a deadly plague that will nearly destroy the human race.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Twelve_monkeysmp.jpg/220px-Twelve_monkeysmp.jpg",
    "https://www.youtube.com/watch?v=15s4Y9ffW_o",
    "http://www.imdb.com/title/tt3148266/"
)

the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "1998",
    "Joel Coen, Ethan Coen",
    "Jeff Bridges, John Goodman, Steve Buscemi, Julianne Moore, Phillip Seymour Hoffman",
    "That's like, your opinion, man!",
    "http://upload.wikimedia.org/wikipedia/en/thumb/3/35/Biglebowskiposter.jpg/220px-Biglebowskiposter.jpg",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y",
    "http://www.imdb.com/title/tt0118715/"
)

# Create an array of the movies and passes to fresh_tomatoes for display
movies = [alien, district_9, gladiator, heat, the_big_lebowski, twelve_monkeys]
fresh_tomatoes.open_movies_page(movies)
