"""
test_config: Configuration file
"""

DEBUG = True
SECRET_KEY = 'key'
USERNAME = 'admin'
invalid_key = 'hello' #variaveis em lowercase nao sao utilizadas

from flask import Flask

app = Flask(__name__)
app.config.from_object('conf_set_var')
#Load all uppercase variables
#from python module conf_set_var.py into 'app.config'

print(app.config['DEBUG'])
print(app.debug) #proxy to 'DEBUG'
print(app.config['SECRET_KEY'])
print(app.secret_key) #proxy to 'SECRET_KEY'
print(app.config['USERNAME'])
#print(app.username) #No proxy for 'USERNAME'
#print(app.config['invalid_key']) #lowercase key not loaded

