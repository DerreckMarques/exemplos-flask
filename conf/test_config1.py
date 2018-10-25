"""
test_config1: Configuration file
"""

class ConfigBase():
    SECRET_KEY = 'your-secret-key'
    DEBUG = False

class ConfigDevelopment(ConfigBase):
    """For development. Inherit from ConfigBase and override some values"""
    DEBUG = True

class ConfigProduction(ConfigBase):
    """For Production. Inherit from ConfigBase and override some values"""
    SECRET_KEY = 'production-secret-key'
    DEBUG = False

from flask import Flask

app = Flask(__name__)
app.config.from_object('test_config1.ConfigDevelopment')
print(app.secret_key)

