import sqlite3

database = sqlite3.connect('data/database.db')
c = database.cursor()

def movieExists(id, user): #checks if a movie exists in the database
    c.execute('SELECT * FROM ' + user)
    b = c.fetchall()
    for r in b:
        if r[0] == str(id):
            return True
    return False

def addMovie(id, user): #adds movie to database
    if (not movieExists(id, user)):
        c.execute("INSERT INTO " + user + " VALUES (" + str(id) + ")")
        database.commit()

def getMovies(user): #returns all movies for a specific user
    c.execute('SELECT * FROM ' + user)
    return c.fetchall()
