import sqlite3

database = sqlite3.connect('data/database.db')

def movieExists(id, user): #checks if a movie exists in the database
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    c.execute('SELECT * FROM ' + user)
    b = c.fetchall()
    for r in b:
        if r[0] == str(id):
            return True
    return False

def addMovie(id, user): #adds movie to database
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    if (not movieExists(id, user)):
        c.execute("INSERT INTO " + user + " VALUES (" + str(id) + ", NULL, NULL)")
        database.commit()

def removeMovie( id, user ):
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    if( movieExists( id, user ) ):
        c.execute("DELETE * FROM %s WHERE movieID == %s;"%(user, str(id) ))
        database.commit()

        
def getMovies(user): #returns all movies for a specific user
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    return c.execute('SELECT movieID FROM ' + user)
    

def getFavs(user):
    database = sqlite3.connect('data/database.db')
    c = database.cursor()
    c.execute("SELECT genre, movie FROM " + user)
    return c.fetchall()
