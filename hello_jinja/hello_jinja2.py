'''#-*-coding: UFT-8-*-'''
"""
Hello_jinja2: get start with jinja2 templates
"""

from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return ""#render_template('j2_query.html')

@app.route('/process', methods=['POST'])
def process():
    _username = request.form.get('username')

    if _username:
        return render_template('j2_response.html', username=_username)
    else:
        return 'Please go back and enter your name...', 400


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0') 
