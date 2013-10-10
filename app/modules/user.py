from flask import Blueprint, request, redirect, render_template, url_for, flash, session

from app import db
from app.forms import LoginForm
from app.models import User

blueprint = Blueprint('user', 
	                   __name__, 
	                   url_prefix='/user', 
	                   static_folder='../static',
	                   template_folder='../templates')

@blueprint.route("/login", methods=['GET', 'POST'])
def login():
	form  = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and (user.password == form.password.data):
			session['user_id'] = user.id 
			flash ('Welcome %s' % user.name)
			return redirect(url_for('user.index'))
		flash('Wrong email or password', 'error-message')
	return render_template('index.html', form=form)

@blueprint.route("/index/", methods=['GET', 'POST'])
def index():
	return render_template('dashboard.html')