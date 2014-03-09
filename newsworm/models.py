from config import db

class Content(db.Model):
	'''
	write a news story to the database specified in __init__.py
	'''
	__tablename__ = 'content'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	link = db.Column(db.String)
	time_scraped = db.Column(db.DateTime)

	def __repr__(self):
		return "<Content(title='{0}', link='{1}', time_scraped='{2}')>".format(self.title, self.link, self.time_scraped)

db.create_all()

