import mysql.connector
from dotenv import dotenv_values

# Get database credentials from .env
db = dotenv_values("../.env")

# Connect to the movies database
conn = mysql.connector.connect(
    host=db["HOST"],
    user=db["USER"],
    password=db["PASSWORD"],
    database=db["DATABASE"]
)

cursor = conn.cursor()

def show_films(cursor, title):
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, "
        "genre_name AS Genre, studio_name AS Studio "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )

    films = cursor.fetchall()

    print("\n-- {} --".format(title))

    for film in films:
        print("Film: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(
            film[0], film[1], film[2], film[3]
        ))

show_films(cursor, "DISPLAYING FILMS")

# Insert The Martian
cursor.execute(
    "INSERT INTO film "
    "(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
    "VALUES ('The Martian', '2015', 144, 'Ridley Scott', 1, 2)"
)

conn.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update Alien to Horror
cursor.execute(
    "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'"
)

conn.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# Delete Gladiator
cursor.execute(
    "DELETE FROM film WHERE film_name = 'Gladiator'"
)

conn.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")