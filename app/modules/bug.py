from flask import Blueprint, request, redirect, render_template, url_for, flash, session

from app import db
from app.forms import BugForm
from app.models import Bug

blueprint = Blueprint('bug', 
	                   __name__, 
	                   url_prefix='/bug', 
	                   static_folder='../static',
	                   template_folder='../templates')

@blueprint.route("/create", methods=['GET', 'POST'])
def index():
	return render_template('bug.html')