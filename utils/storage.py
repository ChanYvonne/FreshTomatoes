import sqlite3

database = sqlite3.connect('data/database.db')

def movieExists(id, user): #checks if a movie exists in the database
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    b = c.execute('SELECT movieID FROM ' + user)
    for r in b:
        if r[0] == id:
            return True
    return False

def addMovie(id, user): #adds movie to database
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    if (not movieExists(id, user)):
        c.execute("INSERT INTO " + user + " VALUES (" + id + ", NULL, NULL)")
        database.commit()

def removeMovie( id, user ): #removes movie from database
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    if( movieExists( id, user ) ):
        c.execute("DELETE FROM " + user + " WHERE movieID = " + id)
        database.commit()

        
def getMovies(user): #returns all movies for a specific user
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    return c.execute('SELECT movieID FROM ' + user)
    

def getFavs(user): #returns favorite genre and movie for user
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    c.execute("SELECT genre, movie FROM " + user)
    return c.fetchall()
