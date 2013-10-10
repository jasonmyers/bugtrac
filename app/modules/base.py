from flask import Blueprint, redirect, render_template, url_for, flash, session

blueprint = Blueprint('base', __name__)

@blueprint.errorhandler(404)
def not_found(error):
	return render_template('404.html')

@blueprint.route('/')
def index():
	return redirect(url_for('user.login'))	