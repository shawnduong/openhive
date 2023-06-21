from __future__ import annotations

from app import db

from typing import Union
from werkzeug.security import generate_password_hash, check_password_hash

# Account modes.
READ_WRITE = 0
READ_ONLY  = 1
WRITE_ONLY = 2

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)

	mode     = db.Column(db.Integer    , unique=False, nullable=False)
	username = db.Column(db.String(256), unique=True , nullable=False)
	password = db.Column(db.String(256), unique=False, nullable=False)

	def __init__(self, username, password, mode=READ_ONLY):

		self.mode = mode

		# Username and password cannot be blank.
		assert username != None and password != None

		# Username must be unique.
		assert User.query.filter_by(username=username).first() == None

		self.username = username
		self.password = generate_password_hash(password, method="sha256")

