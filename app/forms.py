from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email

class BugForm(Form):
	email = TextField('Email address', [Required(), Email()])
	password = PasswordField('Password', [Required()])


class LoginForm(Form):
	email = TextField('Email address', [Required(), Email()])
	password = PasswordField('Password', [Required()])