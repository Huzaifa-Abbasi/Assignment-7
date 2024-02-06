'''Create a program that recommends movies based on user 
preferences. Use variables to store genre, rating, and release year. Write expressions to 
compare movies and suggest matches'''

my_genre = input("Enter the genre ")
my_rating = float(input("Enter the rating "))

movies = {
    "animal": {
        "genre":"action",
           "rating": 6.4,
           "released year": 2023
    },
    "3 idiots":{
        "genre": "comedy",
        "rating": 8.4,
        "released year": 2009
    },
    "spiderman":{
        "genre":"fantasy",
        "rating": 7.4,
        "released year": 2002
    }

}
found_movies = []

for movie_name, details in movies.items():
    if details['genre'] == my_genre and details['rating'] >= my_rating:
        found_movies.append(movie_name)

if found_movies:
    print("Recommended movies based on your preferences:",found_movies)
else:
    print("No matching movies found.")