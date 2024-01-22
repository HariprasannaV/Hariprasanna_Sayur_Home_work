"""
OOP problem.
1. Define a class for movie theatre.
Properties should be Name, current movie, Location, and Owner name.
All fields except Current movie should have value.
Add a constructor to create a new theatre.
Add functions to change the current movie.

In the program, create 5 movie theatres.
List all the theatres in Madurai
List all the theatres that is running the movie "Captain America"

"""


class movie_theatre:
    def __init__(self, name, Location, Owner_name):
        self.name = name
        self.current_movie = ""
        self.Location = Location
        self.owner_name = Owner_name
    def __str__(self):
        return self.name+" "+self.Location+" "+self.current_movie


Theatres = []
inox = movie_theatre("inox","Madurai","Vijay")
vetri = movie_theatre("Vetri","Chennai","Mani")
varadharaja = movie_theatre("varadharaja","Chennai","Hariprasanna")
Gopuram = movie_theatre("Gopuram","Madurai","Manickam")

Theatres.append(inox)
Theatres.append(vetri)
Theatres.append(varadharaja)
Theatres.append(Gopuram)

inox.current_movie = "Captain Miller"
vetri.current_movie = "Ayalaan"
varadharaja.current_movie = "Vikram"
Gopuram.current_movie = "Captain Miller"

print("Madurai Movie Theatres")
for theatre in Theatres:
    if theatre.Location == "Madurai":
        print(theatre.name)
 # print(theatre)
print("Captain miller is running in")
for theatre in Theatres:
    if theatre.current_movie == "Captain Miller":
        print(theatre.name)

inox.current_movie = "Ayalaan"
print("Captain miller is running in")
for theatre in Theatres:
    if theatre.current_movie == "Captain Miller":
        print(theatre.name)