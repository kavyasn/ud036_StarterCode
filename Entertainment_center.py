import fresh_tomatoes
import media

# DDLJ movie: Movie title, Storyline, Poster Image, Youtube tailer link
DDLJ = media.Movie("DDLJ", "Come Fall in Love",
                   "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale\
                   _Dulhania_Le_Jayenge_poster.jpg",
                   "https://www.youtube.com/watch?v=c25GKl5VNeY")

# tzp movie: Movie title, Storyline, Poster image, Youtube trailer
tzp = media.Movie("taare zameen par", "like stars on earth",
                  "https://upload.wikimedia.org/wikipedia/en/b/b4/\
                  Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",
                  "https://www.youtube.com/watch?v=tn_2Ie_jtX8")

# ice age movie: Movie title, Storyline, Poster image, youtube trailer
ice_age = media.Movie("Ice Age", " sub zero heroes",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/\
                      Ice_Age_%282002_film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=akmLI_8oTiI")

# Kung fu panda movie: Movie title, Storyline, poster image, youtube trailer
kung_fu_panda = media.Movie("Kung fu panda", "The Dragon Warrior",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/\
                            Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=WR5MPihJEWQ")

# Madagaskar movie: Movie title, Storyline, Poster image, youtube trailer 
Madagaskar = media.Movie("Madagaskar", "Escape 2 Africa",
                         "https://upload.wikimedia.org/wikipedia/en/7/7f/\
                         Madagascar2poster.jpg",
                         "https://www.youtube.com/watch?v=A45jv8uhZwo")

# I am legend movie: Movie title, Storyline, Poster image, Youtube trailer
I_am_legend = media.Movie("I am Legend", "The last man on Earth is not alone",
                          "https://upload.wikimedia.org/wikipedia/en/d/df/\
                          I_am_legend_teaser.jpg",
                          "https://www.youtube.com/watch?v=dtKMEAXyPkg")

# List data structure is created and all the movies are passed to the media file
movies = [DDLJ, tzp, ice_age, kung_fu_panda, Madagaskar,
          I_am_legend]

# Opens the HTML file in webbrowser with the list of movies
fresh_tomatoes.open_movies_page(movies)




