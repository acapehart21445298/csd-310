""" import statements """
import mysql.connector
import dotenv
from dotenv import dotenv_values


# using our .env file from module-5
secrets = dotenv_values("../module-5/.env")


""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}


""" connect to the movies database """
db = mysql.connector.connect(**config)

cursor = db.cursor()


# --------------------------------------------------
# Query 1 - Display Studio Records
# --------------------------------------------------

print("\n-- DISPLAYING Studio RECORDS --\n")

cursor.execute("SELECT studio_id, studio_name FROM studio")

studios = cursor.fetchall()

for studio in studios:
    print("Studio ID: {}".format(studio[0]))
    print("Studio Name: {}\n".format(studio[1]))


# --------------------------------------------------
# Query 2 - Display Genre Records
# --------------------------------------------------

print("\n-- DISPLAYING Genre RECORDS --\n")

cursor.execute("SELECT genre_id, genre_name FROM genre")

genres = cursor.fetchall()

for genre in genres:
    print("Genre ID: {}".format(genre[0]))
    print("Genre Name: {}\n".format(genre[1]))


# --------------------------------------------------
# Query 3 - Display Short Films
# --------------------------------------------------

print("\n-- DISPLAYING Short Film RECORDS --\n")

cursor.execute(
    "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
)

films = cursor.fetchall()

for film in films:
    print("Film Name: {}".format(film[0]))
    print("Runtime: {}\n".format(film[1]))


# --------------------------------------------------
# Query 4 - Display Films by Director
# --------------------------------------------------

print("\n-- DISPLAYING Director RECORDS in Order --\n")

cursor.execute(
    "SELECT film_name, film_director FROM film "
    "ORDER BY film_director, film_releaseDate DESC"
)

directors = cursor.fetchall()

for director in directors:
    print("Film Name: {}".format(director[0]))
    print("Director: {}\n".format(director[1]))


# close the connection
db.close()