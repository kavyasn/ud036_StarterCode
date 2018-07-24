import fresh_tomatoes
import media


DDLJ = media.Movie("DDLJ", "Come Fall in Love",
                   "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale\
                   _Dulhania_Le_Jayenge_poster.jpg",
                   "https://www.youtube.com/watch?v=c25GKl5VNeY")

tzp = media.Movie("taare zameen par", "like stars on earth",
                  "https://upload.wikimedia.org/wikipedia/en/b/b4/\
                  Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",
                  "https://www.youtube.com/watch?v=tn_2Ie_jtX8")

ice_age = media.Movie("Ice Age", " sub zero heroes",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/\
                      Ice_Age_%282002_film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=akmLI_8oTiI")

kung_fu_panda = media.Movie("Kung fu panda", "The Dragon Warrior",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/\
                            Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=WR5MPihJEWQ")

Madagaskar = media.Movie("Madagaskar", "Escape 2 Africa",
                         "https://upload.wikimedia.org/wikipedia/en/7/7f/\
                         Madagascar2poster.jpg",
                         "https://www.youtube.com/watch?v=A45jv8uhZwo")

I_am_legend = media.Movie("I am Legend", "The last man on Earth is not alone",
                          "https://upload.wikimedia.org/wikipedia/en/d/df/\
                          I_am_legend_teaser.jpg",
                          "https://www.youtube.com/watch?v=dtKMEAXyPkg")

movies = [DDLJ, tzp, ice_age, kung_fu_panda, Madagaskar,
          I_am_legend]

fresh_tomatoes.open_movies_page(movies)




