from sqlalchemy import Column, Boolean, DateTime, VARCHAR, Integer, Binary
from database import Base

class Submissions(Base):
	__tablename__ = 'submissions'
	fotoid = Column(Integer, primary_key=True)
	imgtype = Column(VARCHAR(15))
	data = Column(Binary)
	city = Column(VARCHAR(30))
	caption = Column(VARCHAR(150))
	email = Column(VARCHAR(50))
	date = Column(DateTime)

	def __init__(self, imgtype, data, city, caption, email, date):
		self.imgtype = imgtype
		self.data = data
		self.city = city
		self.caption = caption
		self.email = email
		self.date = date

	def __repr__(self):
		return ('PhotoID: ' + str(self.fotoid))

class Pictures(Base):
	__tablename__ = 'pictures'
	fotoid = Column(Integer, primary_key=True)
	imgtype = Column(VARCHAR(15))
	data = Column(Binary)
	city = Column(VARCHAR(30))
	caption = Column(VARCHAR(150))
	email = Column(VARCHAR(50))
	date = Column(DateTime)
	status = Column(Boolean)

	def __init__(self, imgtype, data, city, caption, email, date, status):
		self.imgtype = imgtype
		self.data = data
		self.city = city
		self.caption = caption
		self.email = email
		self.date = date
		self.status = status

	def __repr__(self):
		return ('PhotoID: ' + str(self.fotoid))
