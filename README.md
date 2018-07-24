# ud036_StarterCode
Source code for a Movie Trailer website.

# About the project 

In this Project We have created a Movie Trailer Website.
In order to do this I have created two files 
1. media.py
2. Entertainment_center.py

In _"Entertainment_center.py"_ file, a constructor "media.Movie" is called and list of six movies "DDLJ", "taare zameen par", "ice age", "kung fu panda", "madagaskar" and " I am legend" is called with instances which includes respective "Movie Title", "Storyline", " Poster image" and "Youtube trailer links". Hence movie objects are instantiated. Movies list is stored in a list and "open_movies_page" function is called which takes these movies as input in order to build the HTML file.

In _"media.py"_, a class called Movie() is created where the properties of the movie "movie_title, movie_storyline, poster_image, trailer_youtube" are encapsulated. From the "Entertainment_center.py" file this constructor is called in order to open the list of movies "DDLJ", "taare zameen par", "ice age", " kung fu panda", "madagaskar" and "I am legend" as a HTML page.

The "fresh_tomatoes.py" file contains a "open_movies_page" function. It takes the list of movies as input and gives the output as the website that shows those movies. 

__Output:__ " On Clicking the poster image of the movie in the "fresh_tomatoes.html" the youtube trailer of the movie is displayed.

## Steps required to Run the application are as follows:

1. Install Python.
2. Create data structure to store list of movies with the details "Movie Title, Story line, Poster image and Youtubetrailer link" which is saved as "Entertainment_center.py"
3. Create a file called "media.py" which contains a class called "Movie()" where the properties of the movie are encapsulated.
4. "fork" the repository and create a copy of "fresh_tomatoes.py"  to work locally into the PC.
5. The fresh_tomatoes.py module has module called "open_movies_page" which takes movies list as input and gives the HTML files with the list of poster images of movie as the output.
6. On clicking any of the poster images the youtube trailer link of the respective movie must be displayed.
