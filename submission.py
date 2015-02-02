import re, datetime
from database import db_session, init_db
from models import Submissions, Pictures

def submit_to_database(form):
	imgtype = '0'
	data = None

	if (form.link.data):
		#Link Example: http://instagram.com/p/yShk-Ivzdt/?modal=true
		match = re.search('p/\w+/', form.link.data)
		if (match):
			imgtype = match.group()[2:-1]

	if (form.picture.data):
		#get file data
		pass

	init_db()
	submission = Submissions(imgtype, data, form.city.data, 
		form.caption.data, form.email.data, datetime.datetime.now())
	db_session.add(submission)
	db_session.commit()

def submissions_info():
	#init_db()
	return Submissions.query.all()

def approve_submissions(fotoID):
	#send info to pictures
	foto = Submissions.query.filter_by(fotoid=fotoID).first()
	
	if (foto):
		new_foto = Pictures(foto.imgtype, foto.data, foto.city, foto.caption, foto.email, foto.date, True)
		db_session.add(new_foto)
		db_session.delete(foto)
		db_session.commit()

def deny_submissions(fotoID):
	#delete entry from submissions
	foto = Submissions.query.filter_by(fotoid=fotoID).first()

	if (foto):
		db_session.delete(foto)
		db_session.commit()
		
		

