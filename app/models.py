from app import db
from sqlalchemy import Sequence

ROLE_USER = 0
ROLE_ADMIN = 1
USER_INACTIVE = 0 
USER_ACTIVE = 1

class User(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer,Sequence('user_id_seq'), primary_key=True)
	name = db.Column(db.String(50), unique=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	role = db.Column(db.SmallInteger, default=ROLE_USER)
	status = db.Column(db.SmallInteger, default=USER_ACTIVE)

	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password


class Project(db.Model):

	__tablename__ = 'project'
	id = db.Column(db.Integer,Sequence('project_id_seq'), primary_key=True)
	name = db.Column(db.String(50), unique=True)

	def __init__(self, name=None):
		self.name = name

class Team(db.Model):

	__tablename__ = 'team'
	id = db.Column(db.Integer,Sequence('team_id_seq'), primary_key=True)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	name = db.Column(db.String(50), unique=True)

	def __init__(self, name=None, project_id=None):
		self.name = name
		self.project_id = project_id


class Bug(db.Model):

	__tablename__ = 'bugs'
	id = db.Column(db.Integer,Sequence('bug_id_seq'), primary_key=True)
	created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
	assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
	severity = db.Column(db.String(10), unique=True)
	title = db.Column(db.String(50))
	description = db.Column(db.String(500))

	def __init__(self, created_by=None, assigned_to=None, project_id=None, team_id=None, severity=None, title=None, description=None):
		self.created_by = created_by
		self.assigned_to = assigned_to
		self.project_id = project_id
		self.team_id = team_id
		self.severity = severity
		self.title = title
		self.description = description


