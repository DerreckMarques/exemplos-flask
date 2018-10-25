"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
app.debug = True
#
@app.route('/')
def main():
    return '\nHello Flask\n\n'

if __name__ == '__main__':
    app.run(debug=True)
