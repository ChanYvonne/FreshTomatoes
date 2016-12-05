from flask import Flask, session, request, url_for, redirect, render_template
from utils import authen
app = Flask(__name__)
app.secret_key = "SOME_KEY"

@app.route("/")
def root():
    if( 'username' in session.keys() ):
        return redirect(url_for( 'home' ))
    else:
        return redirect(url_for( 'login' ))

@app.route("/login/")
def login( **keyword_parameters ):
    message = ""
    if( 'message' in keyword_parameters):
        message = keyword_parameters['message']
    elif( 'message' in request.args ):
        message = request.args.get('message')
    return render_template('login.html', message = message)

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
            return redirect(url_for('login', message = "Registration Successful"))
        else:
            return redirect(url_for('login', message = val))
    else:
        return redirect(url_for( 'root' ) )

@app.route("/home/")
def home():
    render_template("home.html")
    

if __name__ == "__main__":
    app.debug = True
    app.run()

