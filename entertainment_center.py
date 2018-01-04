import fresh_tomatoes
import media
""" A list of movie attributes are stored and used to create objects of type Movie.
    The objects are then passed to the open_movies_page function of the fresh_tomatoes module."""
    
# Storing the information about movies in a list of dictionary
list_of_movies = [{'title': "Toy Story",
                   'story': "A story of a boy and his toys that come to life",
                   'poster': "http://www.movieposter.com/posters/archive/main/15/A70-7642",
                   'trailer': "https://www.youtube.com/watch?v=KYz2wyBy3kc"},
                  {'title': "Avatar",
                   'story': "A marine on an alien planet",
                   'poster': "http://www.freemovieposters.net/posters/avatar_2009_2681_poster.jpg",
                   'trailer': "https://www.youtube.com/watch?v=5PSNL1qE6VY"},
                  {'title': "Star Wars",
                   'story': "The rebels dispatch to Endor to destroy a more powerful Death Star.",
                   'poster': "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                   'trailer': "https://www.youtube.com/watch?v=7L8p7_SLzvU"},
                  {'title': "Serendipity",
                   'story': "A couple search for each other years after the night they first met, fell in love, and separated.",
                   'poster': "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzOTQ3Nl5BMl5BanBnXkFtZTYwMjI1NzU5._V1_QL50_.jpg",
                   'trailer': "https://www.youtube.com/watch?v=ePU2Ux9JIMM"},
                  {'title': "La La Land",
                   'story': "While navigating their careers in Los Angeles, a pianist and an actress fall in love.",
                   'poster': "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_QL50_SY1000_SX675_AL_.jpg",
                   'trailer': "https://www.youtube.com/watch?v=0pdqf4P9MB8&t=3s\
                   "},
                  {'title': "Ferdinand",
                   'story': "After Ferdinand, a bull with a big heart, is mistaken for a dangerous beast, he is captured and torn from his home.",
                   'poster': "https://images-na.ssl-images-amazon.com/images/M/MV5BOTIwMDI0NjQ4OF5BMl5BanBnXkFtZTgwNjU0MzAyNDM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                   'trailer': "https://www.youtube.com/watch?v=n7RkOfN8KvE"}
                  ]
# Initializing a new list that will contain all the movie objects
movies = []
# Creating instances for different movies and adding them to the list
for item in list_of_movies:
    movies.append(media.Movie(item['title'], item['story'], item['poster'],
                      item['trailer']))

# Calling the open_movies_page function present in the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
