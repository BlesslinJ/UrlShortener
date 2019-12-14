from .database import db
from datetime import datetime
import string
from random import choices
from flask import request
from .forms import UrlForm

class Urls(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(512), nullable=False)
	short_url = db.Column(db.String(20), nullable=False, unique=True)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.short_url = self.create_short_link()

	def create_short_link(self):
		d_short_url = request.form['Word']		
		link = self.query.filter_by(short_url=d_short_url).first()
		if link:
			short_url = d_short_url + ''.join(choices(string.digits, k=3))
			return short_url
		short_url = d_short_url	
		return short_url