"""
wtfeg1_form: Flask-WTF Example 1 - Login Form
"""

#Import 'FlaskForm' from 'flask_wtf, NOT 'wtforms'
#from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
#Fields and validators from 'wtforms'
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length



#Define the 'LoginForm' class by sub-classing 'Form'
class LoginForm(FlaskForm):
    #this form contains two fields with input validators
    username = StringField('User Name:', validators=[InputRequired(), Length(max=20)])
    passwd = PasswordField('Password:', validators=[Length(min=4, max=16)])