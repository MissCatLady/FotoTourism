import os
from flask import Flask
from flask import render_template, request, flash
from forms import addPicture
from werkzeug import secure_filename
from database import db_session
from submission import submit_to_database, submissions_info, approve_submissions, deny_submissions
from populate import populate_main

UPLOAD_FOLDER = '/static/imgs/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = 'CHANGETHISLATER'

def allowed_file(filename):
	return ("." in filename and 
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS)

@app.route('/')
def index():
	images = populate_main()
	return render_template('index.html', images=images)

@app.route('/submit', methods=('GET', 'POST'))
def add_picture():
	form = addPicture(request.form)

	if request.method == 'POST':
		if form.validate():
			flash('Thanks for your submission!')
			submit_to_database(form)

		else:
			flash('Please fill out all fields correctly.')

	return render_template('submit.html', form=form)

@app.route('/submissions')
def review_submissions():
	submissions = submissions_info()
	return render_template('submissions.html', submissions=submissions)

@app.route('/submissions/approve/<fotoID>')
def approve(fotoID):
	approve_submissions(fotoID)
	return review_submissions()

@app.route('/submissions/deny/<fotoID>')
def deny(fotoID):
	deny_submissions(fotoID)
	return review_submissions()

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()


if __name__ == '__main__':
	app.run(debug=True)