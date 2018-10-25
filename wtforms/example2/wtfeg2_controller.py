"""
wtfeg2_controller: Flask-wtf Example 2 - processing the login Form
"""

import os, binascii
from flask import Flask, render_template, flash, redirect, url_for
from wtfeg2_form import LoginForm

#initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY']=binascii.hexlify(os.urandom(24))
#Flask-wtf: Needed for CSRF

@app.route('/', methods=['get', 'post'])#First request via GET, subsequent requests via POST
def main():
    # Construct an instance of LoginForm
    form = LoginForm()

    if form.validate_on_submit(): #POST request with valid input ?
        if (form.username.data == 'Peter' and form.passwd.data == 'xxxx'):
            #Render an HTML page, with the login form instance created
            return redirect(url_for('startapp'))
        else:
            flash('Wrong username or password')
    
    return render_template('wtfeg2_login.html', form=form)


@app.route('/startapp')
def startapp():
    return "The app is here!"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 #Not Found

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


