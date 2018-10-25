import os, binascii
from flask import Flask, render_template
from wtfeg1_form import LoginForm

#initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY']=binascii.hexlify(os.urandom(24))
#Flask-wtf: Needed for CSRF

@app.route('/')
def main():
    # Construct an instance of LoginForm
    _form = LoginForm()

    #Render an HTML page, with the login form instance created
    return render_template('wtfeg1_login.html', form=_form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
