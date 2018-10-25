# -*- coding: UTF-8 -*-

"""
test_session: Testing Flask's session
"""

from flask import Flask, session, redirect, url_for, escape, request, g
import time

app = Flask(__name__)
app.config['SECRET_KEY']='Your Secret Key'

@app.route('/')
def main():
    if 'username' in session:
        return 'You are alredy logged in as %s' % escape(session['username'])
    return (redirect(url_for('login')))

@app.route('/login', methods=['GET', 'POST'])
def login():
    #for subsequent POST requests
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username #save in session
        return 'Logined in as %s ' % escape(username) 

    #For the initial GET request
    return """
        <form method='POST'>
        Enter your name: <input type='text' name='username'>
        <input type='submit' value='Login'>
        </form>"""

@app.route('/logout')
def logout():
    #Remove 'username' from the session if it exits
    session.pop('username', None)
    return redirect(url_for('main'))

@app.before_request
def before_request():
    g.start_time = time.time()

@app.teardown_request
def teardown_request(exception=None):
    time_taken = time.time() - g.start_time
    print("teste " + str(time_taken))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')