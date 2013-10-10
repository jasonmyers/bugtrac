from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.modules import base, bug, user
app.register_blueprint(base.blueprint)
app.register_blueprint(bug.blueprint)
app.register_blueprint(user.blueprint)