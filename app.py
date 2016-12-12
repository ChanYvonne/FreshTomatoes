from flask import Flask, session, request, url_for, redirect, render_template
from utils import authen, interactAPI, storage
app = Flask(__name__)
app.secret_key = "SOME_KEY"

@app.route("/")
def root():
    if loggedIn():
        return redirect(url_for('home', user = session['username']))
    else:
        return redirect(url_for('login'))

@app.route("/login/")
def login(**keyword_parameters):
    message = ""
    if('message' in keyword_parameters):
        message = keyword_parameters['message']
    elif('message' in request.args):
        message = request.args.get('message')
    return render_template('login.html', message = message)

@app.route("/register/")
def register(**keyword_parameters):
    message = ""
    if('message' in keyword_parameters):
        message = keyword_parameters['message']
    elif('message' in request.args):
        message = request.args.get('message')
    return render_template('register.html', message = message)

@app.route("/authenticate/", methods = ["POST"])
def authenicate():
    dbData = authen.dbHandler()
    userNames = dbData['usernames']
    passWords = dbData['passwords']
    if request.form['account'] == 'Login':
        val = authen.authenticate(request.form, userNames, passWords)
        if val == True :
            session['username'] = request.form['user']
            return redirect(url_for('root'))
        else:
            return redirect(url_for('login', message = val))
    elif request.form['account'] == 'Register':
        val = authen.register(request.form, userNames, passWords)
        if val == True :
            return redirect(url_for('login', message = "Registration Successful",))
        else:
            return redirect(url_for('register', message = val))
    else:
        return redirect(url_for('root'))

@app.route("/search/", methods = ["GET"])
def search():
    if('m' in request.args):
        query = request.args.get('m')
        results = interactAPI.get_search_details_m(interactAPI.get_ids(query, 'm'))
        return render_template('search_results.html', query = query, results = results, id = id, user = session['username'])
    elif('a' in request.args):
        query = request.args.get('a')
        results = interactAPI.get_search_details_a(interactAPI.get_ids(query, 'a'))
        return render_template('search_results.html', query = query, results = results, id = id, user = session['username'])
    else:
        return " someone done goofed "

@app.route("/movie/<movieid>")
def movie(movieid):
    if (not loggedIn()):
        return redirect(url_for('login'))

    results = interactAPI.get_movie_details(int(movieid))
    link = interactAPI.getLink(int(movieid))
    return render_template('movie.html', title = results[0], year = results[1], blurb = results[2], quote = results[3], image_url = results[4], link = link [0], linkDescription = link [1], reviewuser = session['username'])


@app.route("/home/")
def home(**keyword_parameters):
    if (not loggedIn() ):
        return redirect(url_for('login'))
    elif('user' in request.args):
        return render_template('home.html', user = request.args.get('user'))
    else:
        return render_template('home.html', user = session['username'])

@app.route("/actorSearch/")
def act():
    if (not loggedIn()):
        return redirect(url_for('login'))
    return render_template('actorSearch.html', user = session['username']);

@app.route("/list/")
def list():
    result = []
    for r in getMovies (session ['username']):
        result += r
        print result
    return render_template('list.html', result = result, user = session['username'])

@app.route("/account/")
def account():
    return render_template("account.html")

@app.route("/logout/")
def logout():
    session.pop('username')
    return redirect(url_for('root'))

def loggedIn():
    return ('username' in session)

if __name__ == "__main__":
    app.debug = True
    app.run()
