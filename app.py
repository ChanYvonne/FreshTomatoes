from flask import Flask, session, request, url_for, redirect, render_template
from utils import authen, interactAPI
app = Flask(__name__)
app.secret_key = "SOME_KEY"

@app.route("/")
def root():
    if 'username' in session:
        return redirect( url_for( 'home', user = session['username'] ) )
    else:
        return redirect( url_for( 'home' ) )

@app.route("/login/")
def login( **keyword_parameters ):
    message = ""
    if( 'message' in keyword_parameters):
        message = keyword_parameters['message']
    elif( 'message' in request.args ):
        message = request.args.get('message')
    return render_template('login.html', message = message)

@app.route("/register/")
def register( **keyword_parameters ):
    message = ""
    if( 'message' in keyword_parameters):
        message = keyword_parameters['message']
    elif( 'message' in request.args ):
        message = request.args.get('message')
    return render_template('register.html', message = message)

@app.route("/authenticate/", methods = ["POST"] )
def authenicate():
    dbData = authen.dbHandler( )
    userNames = dbData['usernames']
    passWords = dbData['passwords']
    if request.form['account'] == 'Login':
        val = authen.authenticate(request.form, userNames, passWords )
        if val == True :
            session['username'] = request.form['user']
            return redirect(url_for('root'))
        else:
            return redirect(url_for('login', message = val))
    elif request.form['account'] == 'Register':
        val = authen.register(request.form, userNames, passWords)
        if val == True :
            return redirect(url_for('login', message = "Registration Successful", ))
        else:
            return redirect(url_for('register', message = val))
    else:
        return redirect(url_for( 'root' ) )

@app.route("/search/", methods = ["GET"])
def search():
    query = request.args.get('q')
    results = interactAPI.get_search_details(query)
    if( 'username' in session ):
        return render_template('search_results.html', query = query, results = results, id = id, user = session['username'] )
    else:
        return render_template('search_results.html', query = query, results = results, id = id)
    


@app.route("/movie/<movieid>")
def movie(movieid):
    #id = request.args.get('id')
    results = interactAPI.get_movie_details(int(movieid))
    if( 'username' in session ):
        return render_template('movie.html', title = results[0], year = results[1], blurb = results[2], quote = results[3], image_url = results[4], user = session['username'])
    else:
        return render_template('movie.html', title = results[0], year = results[1], blurb = results[2], quote = results[3], image_url = results[4])
    

@app.route("/home/")
def home(**keyword_parameters):
    if( 'user' in request.args ):
        return render_template('home.html', user = request.args.get('user')) 
    elif ( 'username' in session ):
        return render_template('home.html', user = session['username'])
    else:
        return render_template('home.html')

@app.route("/actorSearch/")
def act():
    if( 'username' in session ):
        return render_template('actorSearch.html', user = session['username']);
    else:
        return render_template('actorSearch.html');
    
    

@app.route("/account/")
def account():
    return render_template("account.html")

@app.route("/logout/")
def logout():
    session.pop('username')
    return redirect(url_for( 'root' ) )

if __name__ == "__main__":
    app.debug = True
    app.run()

