# -*- coding: UTF-8 -*-
"""
test_logging: Testing logging under Flask
"""

from flask import Flask
app = Flask(__name__)

#Create a file handler
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('test.log')
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    "%(asctime)s|%(levelname)s|%(message)s|%(pathname)s:%(lineno)d"
))

app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

app.logger.debug('A debug message')
app.logger.info('An info message')
app.logger.warning('A warning message')
app.logger.error('An error message')
app.logger.critical('A critical message')

@app.route('/')
def main():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

